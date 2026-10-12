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
import importlib.util
import os
import sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "cmpm", os.path.join(TOOLS, "compare-manifests.py"))
cmpm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cmpm)

NOISE_PREFIXES = ("home/.hatch-db-change-signals/",)
GROUP_LIMIT = 40


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
                items.append(f"`{name}` — SKILL.md updated")
            else:
                items.append(f"`{name}` — {len(files)} file(s): "
                             + ", ".join(f"`{f.split('/')[-1]}`"
                                          for f in sorted(files)[:4]))
        section(f"Shipped skills ({len(skills)} changed)", items, lambda s: s)
    if docs:
        items = [fmt_size_change(p.split('/')[-1],
                                 before[p]["size_bytes"], after[p]["size_bytes"])
                 for p in sorted(docs)]
        section("Product docs (`home/docs/`, %d changed)" % len(docs), items,
                lambda s: s)
    if other:
        section("Other (%d changed)" % len(other), sorted(other),
                lambda p: f"`{p}`")
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
