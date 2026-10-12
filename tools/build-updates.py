#!/usr/bin/env python3
"""Generate updates.md: a muse-watch-style "what's new" feed for the repo.

Reads CHANGELOG.md (hand-written prose entries) and builds.md (auto-appended
release rows) and writes updates.md, newest first, with dated badges and
what-changed detail bullets — the same feed shape as the muse watch dashboard.

Run from anywhere:  python3 tools/build-updates.py
Idempotent: same inputs produce byte-identical output.
"""
import os
import re
import sys
from datetime import date

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHANGELOG = os.path.join(REPO, "CHANGELOG.md")
BUILDS = os.path.join(REPO, "builds.md")
OUT = os.path.join(REPO, "updates.md")
FEED_BUILD_LIMIT = 30  # full history stays in builds.md


def github_anchor(text):
    """GitHub's heading slug: lowercase, drop punctuation, spaces -> hyphens."""
    a = text.lower()
    a = re.sub(r"[^a-z0-9 _-]", "", a)
    return re.sub(r"\s+", "-", a.strip())


def parse_changelog():
    entries = []
    text = open(CHANGELOG).read()
    parts = re.split(r"(?m)^## ", text)
    for part in parts[1:]:
        head, _, body = part.partition("\n")
        m = re.match(r"(\d{4}-\d{2}-\d{2})\s*-\s*(.*)", head.strip())
        if not m:
            continue
        day, title = m.group(1), m.group(2).strip()
        entries.append({"day": day, "title": title, "body": body.strip(),
                        "kind": "changelog"})
    return entries


def badge_for(title):
    t = title.lower()
    if any(k in t for k in ("rebuild", "deep-dive", "rewrite", "redraw",
                            "diagram", "chapter", "book", "guide", "doc",
                            "field guide")):
        return "DOCS"
    if any(k in t for k in ("build", "release", "archive", "launch")):
        return "NEW BUILD" if "build" in t or "release" in t else "UPDATE"
    if any(k in t for k in ("fix", "correct", "repair")):
        return "FIX"
    return "UPDATE"


ROW_RE = re.compile(
    r"^\|\s*`([0-9a-f]{10})`\s*\|\s*([0-9T:\-Z]+)\s*\|\s*([0-9\-]+)[^|]*\|\s*(.*?)\s*\|?\s*$")


def parse_builds():
    entries = []
    pending_note = []
    for line in open(BUILDS):
        line = line.rstrip("\n")
        m = ROW_RE.match(line)
        if m:
            if pending_note:
                entries[-1]["note"] = " ".join(pending_note).strip()
                pending_note = []
            commit, built_at, detected, archive = m.groups()
            link = None
            lm = re.search(r"\[Release\]\(([^)]+)\)", archive)
            if lm:
                link = lm.group(1)
            else:
                # newer rows record the release in prose, not a link; the
                # tag name is deterministic, so build the URL directly
                link = ("https://github.com/mikezio/muse-runtime/releases/"
                        "tag/build-%s" % commit)
            entries.append({"day": detected, "commit": commit,
                            "built_at": built_at, "archive": archive.strip(),
                            "link": link, "kind": "build"})
        elif line.startswith("- ") and entries and pending_note is not None:
            pending_note.append(line[2:].strip())
    if pending_note and entries:
        entries[-1]["note"] = " ".join(pending_note).strip()
    return entries


def trim_body(body, limit=12):
    lines = [l for l in body.splitlines()]
    kept = []
    for l in lines:
        s = l.strip()
        if not s:
            continue
        kept.append(l)
        if len(kept) >= limit:
            break
    return kept, len(lines) > len(kept)


def render_changelog(e):
    badge = badge_for(e["title"])
    anchor = github_anchor("## %s - %s" % (e["day"], e["title"]))
    out = ["## %s · **%s** — %s\n" % (e["day"], badge, e["title"])]
    bullets, truncated = trim_body(e["body"])
    for b in bullets:
        s = b.strip()
        if s.startswith("- ") or s.startswith("* "):
            out.append(s)
        else:
            out.append("- " + s)
    if truncated:
        out.append("- …full entry in [CHANGELOG.md](CHANGELOG.md#%s)" % anchor)
    return "\n".join(out)


def short_archive_text(archive):
    # The archive cell often carries run-level upload notes; keep the gist.
    a = re.sub(r"\s+", " ", archive)
    if len(a) > 220:
        a = a[:217] + "…"
    return a


def render_build(e):
    rel = ("[Release](%s)" % e["link"]) if e["link"] else "no release page"
    lines = ["## %s · **NEW BUILD** — runtime build `%s`\n" % (e["day"], e["commit"]),
             "- Built %s, detected %s." % (e["built_at"], e["day"]),
             "- %s — %s." % (rel, short_archive_text(e["archive"]))]
    if e.get("note"):
        n = re.sub(r"\s+", " ", e["note"])
        if len(n) > 220:
            n = n[:217] + "…"
        lines.append("- %s" % n)
    return "\n".join(lines)


def main():
    changelog = parse_changelog()
    builds = parse_builds()
    feed = changelog + builds
    feed.sort(key=lambda e: (e["day"], 0 if e["kind"] == "changelog" else 1),
              reverse=True)

    today = date.today().isoformat()
    out = [
        "# What's new\n",
        "_Last updated: %s (ET). Generated from [CHANGELOG.md](CHANGELOG.md) "
        "and [builds.md](builds.md) — newest first. "
        "The full release history lives in builds.md._\n" % today,
    ]
    shown_builds = 0
    total_builds = len(builds)
    for e in feed:
        if e["kind"] == "build":
            if shown_builds >= FEED_BUILD_LIMIT:
                continue
            shown_builds += 1
            out.append(render_build(e) + "\n")
        else:
            out.append(render_changelog(e) + "\n")
    if total_builds > shown_builds:
        out.append("_Showing the %d most recent builds; the complete list is "
                   "in [builds.md](builds.md)._\n" % shown_builds)

    text = "\n".join(out).rstrip("\n") + "\n"
    old = open(OUT).read() if os.path.exists(OUT) else None
    if old != text:
        open(OUT, "w").write(text)
        print("updates.md written (%d entries)" % len(feed))
    else:
        print("updates.md already current")


if __name__ == "__main__":
    sys.exit(main())
