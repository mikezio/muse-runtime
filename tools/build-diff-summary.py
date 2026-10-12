#!/usr/bin/env python3
"""Summarize what changed between two runtime archive manifests.

Usage:
  build-diff-summary.py <prev.manifest.txt> <new.manifest.txt> \
      --prev-commit <10char> --new-commit <10char> [--new-built-at <iso>]

Prints markdown for GitHub release notes: grouped, human-readable, with
ephemeral runtime noise (db change-signal churn) collapsed instead of listed.

Exit 0 always; prints a short note when there is no meaningful diff.
"""
import argparse
import difflib
import importlib.util
import os
import re
import subprocess
import sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "cmpm", os.path.join(TOOLS, "compare-manifests.py"))
cmpm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cmpm)

NOISE_PREFIXES = ("home/.hatch-db-change-signals/",)
GROUP_LIMIT = 40
DEEP_DIFF_LIMIT = 12       # max files with inside-the-file detail
DEEP_DIFF_MAX_BYTES = 512 * 1024
TEXT_EXTS = (".md", ".txt", ".json", ".yaml", ".yml", ".sh", ".py",
             ".toml", ".cfg", ".ini", ".mdwn")


def frontmatter_desc(data):
    try:
        text = data.decode("utf-8", "replace")
    except Exception:
        return ""
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return ""
    fm = m.group(1)
    d = re.search(r'^description:\s*"(.*)"\s*$', fm, re.M)
    if not d:
        d = re.search(r"^description:\s*(.+?)\s*$", fm, re.M)
    return (d.group(1) if d else "").strip()


def describe_inside(old_data, new_data):
    """What changed inside a text file: line counts + changed sections."""
    try:
        old_t = old_data.decode("utf-8", "replace")
        new_t = new_data.decode("utf-8", "replace")
    except Exception:
        return "content changed"
    parts = []
    old_d, new_d = frontmatter_desc(old_data), frontmatter_desc(new_data)
    if old_d != new_d and (old_d or new_d):
        parts.append("description updated" if old_d and new_d
                     else "description added" if new_d else "description removed")
    old_l, new_l = old_t.splitlines(), new_t.splitlines()
    sm = difflib.SequenceMatcher(None, old_l, new_l, autojunk=False)
    added_n = removed_n = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ("replace", "delete"):
            removed_n += i2 - i1
        if tag in ("replace", "insert"):
            added_n += j2 - j1
    if added_n or removed_n:
        parts.append(f"+{added_n}/-{removed_n} lines")
    # which markdown sections changed
    if new_t.lstrip().startswith("#"):
        bounds = [(m.start(), m.group(1)) for m in
                  re.finditer(r"^#{1,3}\s+(.+?)\s*$", new_t, re.M)]
        starts = []
        pos = 0
        for ln in new_t.splitlines(keepends=True):
            starts.append(pos)
            pos += len(ln)

        def section_for(p):
            sec = None
            for s, name in bounds:
                if s <= p:
                    sec = name
                else:
                    break
            return sec

        secs = set()
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag != "equal":
                for j in range(j1, min(j2, len(starts))):
                    s = section_for(starts[j])
                    if s:
                        secs.add(s)
        if secs:
            parts.append("sections: " + ", ".join(sorted(secs)[:4]))
    return "; ".join(parts) if parts else "content changed"


def looks_textual(path, size):
    if size > DEEP_DIFF_MAX_BYTES:
        return False
    if path.startswith("opt/bin/"):
        return False
    return path.lower().endswith(TEXT_EXTS)


def zip_read(zip_path, arc_path):
    """Read one file from a zip without extracting; None on any failure."""
    try:
        r = subprocess.run(["unzip", "-p", zip_path, arc_path],
                           capture_output=True, timeout=120)
    except Exception:
        return None
    return r.stdout if r.returncode == 0 and r.stdout else None


def human(n):
    n = abs(n)
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.1f} {unit}" if unit != "B" else f"{n} B"
        n /= 1024


def is_noise(path):
    return path.startswith(NOISE_PREFIXES)


def diff_all(before, after):
    """Full set diff without compare-manifests' display limit."""
    old, new = set(before), set(after)
    return {
        "added": sorted(new - old),
        "removed": sorted(old - new),
        "changed": sorted(p for p in old & new if before[p] != after[p]),
        "total_after": len(new),
    }


def skill_of(path):
    # opt/hatch/skills/<name>/...
    parts = path.split("/")
    if len(parts) >= 4 and parts[0] == "opt" and parts[1] == "hatch" \
            and parts[2] == "skills":
        return parts[3]
    return None


def fmt_size_change(name, b0, b1):
    if human(b0) == human(b1):
        return f"`{name}` ({human(b0)}, {b1 - b0:+,d} bytes)"
    return f"`{name}` ({human(b0)} → {human(b1)})"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prev_manifest")
    ap.add_argument("new_manifest")
    ap.add_argument("--prev-commit", required=True)
    ap.add_argument("--new-commit", required=True)
    ap.add_argument("--new-built-at", default="")
    ap.add_argument("--prev-zip", default="",
                    help="previous build's archive zip: enables inside-the-file "
                         "detail by extracting old+new content")
    ap.add_argument("--new-zip", default="",
                    help="new build's archive zip (paired with --prev-zip)")
    args = ap.parse_args()

    try:
        before = cmpm.read_manifest(args.prev_manifest)
        after = cmpm.read_manifest(args.new_manifest)
    except (ValueError, OSError) as e:
        print(f"_Could not diff manifests: {e}_")
        return 0

    res = diff_all(before, after)
    added = [p for p in res["added"] if not is_noise(p)]
    removed = [p for p in res["removed"] if not is_noise(p)]
    changed = [p for p in res["changed"] if not is_noise(p)]
    noise_n = (len(res["added"]) + len(res["removed"]) + len(res["changed"])
               - len(added) - len(removed) - len(changed))

    total = len(added) + len(removed) + len(changed)
    lines = [f"## What changed vs build `{args.prev_commit}`", ""]
    if args.new_built_at:
        lines.append(f"Build `{args.new_commit}` ({args.new_built_at}).")
    if total == 0:
        lines.append("No file changes vs the previous build"
                     + (" (only ephemeral runtime state rotated)." if noise_n else "."))
        print("\n".join(lines))
        return 0
    lines.append(
        f"{total} file{'s' if total != 1 else ''} changed "
        f"({len(added)} added, {len(removed)} removed, {len(changed)} modified) "
        f"out of {res['total_after']:,} archived."
    )

    # group the modified files
    bins_same, bins_sized = [], []
    skills = {}
    docs = []
    other = []
    for p in changed:
        if p.startswith("opt/bin/"):
            name = p.split("/")[-1]
            b0, b1 = before[p]["size_bytes"], after[p]["size_bytes"]
            if b0 == b1:
                bins_same.append(name)
            else:
                bins_sized.append((name, b0, b1))
        elif skill_of(p):
            skills.setdefault(skill_of(p), []).append(p)
        elif p.startswith("home/docs/"):
            docs.append(p)
        else:
            other.append(p)

    # inside-the-file detail: for changed text files, extract old bytes from
    # the previous zip and new bytes from the new zip, then summarize the
    # content diff (line counts, changed sections). Binaries keep size notes.
    inside = {}
    deep_ok = (args.prev_zip and args.new_zip
               and os.path.exists(args.prev_zip) and os.path.exists(args.new_zip))
    if deep_ok:
        candidates = [p for p in changed
                      if looks_textual(p, after[p]["size_bytes"])]
        for p in candidates[:DEEP_DIFF_LIMIT]:
            old_b = zip_read(args.prev_zip, "runtime/" + p)
            new_b = zip_read(args.new_zip, "runtime/" + p)
            if old_b is None or new_b is None:
                continue
            if b"\x00" in old_b[:8192] or b"\x00" in new_b[:8192]:
                continue
            inside[p] = describe_inside(old_b, new_b)

    def sub(p):
        return f"\n  - {inside[p]}" if p in inside else ""

    def section(title, items, fmt):
        lines.append("")
        lines.append(f"### {title}")
        for it in items[:GROUP_LIMIT]:
            lines.append(f"- {fmt(it)}")
        if len(items) > GROUP_LIMIT:
            lines.append(f"- …and {len(items) - GROUP_LIMIT} more")

    if bins_sized or bins_same:
        items = ([fmt_size_change(n, b0, b1) for n, b0, b1 in sorted(bins_sized)]
                 + [f"`{n}` (rebuilt, same size)" for n in sorted(bins_same)])
        section(f"Binaries (`opt/bin/`, {len(items)} changed)", items, lambda s: s)
    if skills:
        items = []
        for name in sorted(skills):
            files = skills[name]
            if files == [f"opt/hatch/skills/{name}/SKILL.md"]:
                items.append((files[0], f"`{name}`: SKILL.md updated"))
            else:
                items.append((files[0], f"`{name}`: {len(files)} file(s): "
                             + ", ".join(f"`{f.split('/')[-1]}`"
                                          for f in sorted(files)[:4])))
        section(f"Shipped skills ({len(skills)} changed)",
                [t + sub(p) for p, t in items], lambda s: s)
    if docs:
        items = [(p, fmt_size_change(p.split('/')[-1],
                                     before[p]["size_bytes"],
                                     after[p]["size_bytes"]))
                 for p in sorted(docs)]
        section("Product docs (`home/docs/`, %d changed)" % len(docs),
                [t + sub(p) for p, t in items], lambda s: s)
    if other:
        section("Other (%d changed)" % len(other), sorted(other),
                lambda p: f"`{p}`{sub(p)}")
    if added:
        section("Added (%d)" % len(added), sorted(added), lambda p: f"`{p}`")
    if removed:
        section("Removed (%d)" % len(removed), sorted(removed),
                lambda p: f"`{p}`")
    if noise_n:
        lines.append("")
        lines.append(f"_Ephemeral runtime state rotated ({noise_n} db "
                     f"change-signal files, not meaningful)._")
    lines.append("")
    lines.append("Full per-file hashes: see the attached manifest. "
                 "Compare any two manifests locally with "
                 "`python3 tools/compare-manifests.py before.manifest.txt after.manifest.txt`.")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
