#!/usr/bin/env python3
"""Compare archive-runtime.sh manifests without opening or executing archives."""

import argparse
import json
from pathlib import Path, PurePosixPath
import re
import sys


RECORD = re.compile(r"([0-9a-fA-F]{64})  ([0-9]+)  (.+)")


def safe_path(value):
    """Normalize the generator's ./ prefix, rejecting ambiguous/unsafe names."""
    if value.startswith("./"):
        value = value[2:]
    if (not value or PurePosixPath(value).is_absolute()
            or any(part in ("", ".", "..") for part in value.split("/"))
            or "\\" in value
            or any(ord(char) < 32 or ord(char) == 127 for char in value)):
        raise ValueError("invalid relative path")
    return value


def read_manifest(filename):
    records = {}
    with Path(filename).open(encoding="utf-8", newline="") as source:
        for number, line in enumerate(source, 1):
            line = line.rstrip("\n")
            match = RECORD.fullmatch(line)
            if not match:
                raise ValueError(f"{filename}:{number}: expected SHA256  SIZE_BYTES  RELATIVE_PATH")
            digest, size, name = match.groups()
            try:
                name = safe_path(name)
            except ValueError as error:
                raise ValueError(f"{filename}:{number}: {error}") from error
            if name in records:
                raise ValueError(f"{filename}:{number}: duplicate normalized path")
            records[name] = {"sha256": digest.lower(), "size_bytes": int(size)}
    return records


def compare(before, after, limit=20, prefix=None):
    if prefix:
        prefix = safe_path(prefix.rstrip("/"))
        before = {p: v for p, v in before.items() if p == prefix or p.startswith(prefix + "/")}
        after = {p: v for p, v in after.items() if p == prefix or p.startswith(prefix + "/")}
    old, new = set(before), set(after)
    added = sorted(new - old)
    removed = sorted(old - new)
    changed = sorted(p for p in old & new if before[p] != after[p])
    result = {
        "scope": prefix or ".",
        "counts": {"before": len(old), "after": len(new), "added": len(added),
                   "removed": len(removed), "changed": len(changed),
                   "unchanged": len(old & new) - len(changed)},
        "bytes": {"before": sum(v["size_bytes"] for v in before.values()),
                  "after": sum(v["size_bytes"] for v in after.values())},
        "limit_per_category": limit,
        "added": [{"path": p, **after[p]} for p in added[:limit]],
        "removed": [{"path": p, **before[p]} for p in removed[:limit]],
        "changed": [{"path": p, "before": before[p], "after": after[p]}
                    for p in changed[:limit]],
        "omitted": {"added": max(0, len(added) - limit),
                    "removed": max(0, len(removed) - limit),
                    "changed": max(0, len(changed) - limit)},
    }
    result["bytes"]["delta"] = result["bytes"]["after"] - result["bytes"]["before"]
    return result


def nonnegative(value):
    try:
        number = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("must be an integer >= 0") from error
    if number < 0:
        raise argparse.ArgumentTypeError("must be an integer >= 0")
    return number


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("before", help="older SHA256/size/path manifest")
    parser.add_argument("after", help="newer SHA256/size/path manifest")
    parser.add_argument("--limit", type=nonnegative, default=20,
                        help="maximum displayed paths per category, including JSON (default: 20; 0: counts only)")
    parser.add_argument("--prefix", help="restrict to a relative path or directory, e.g. opt/skills")
    parser.add_argument("--json", action="store_true", help="emit structured JSON")
    args = parser.parse_args(argv)
    try:
        result = compare(read_manifest(args.before), read_manifest(args.after), args.limit, args.prefix)
    except (OSError, UnicodeError, ValueError) as error:
        parser.exit(2, f"error: {error}\n")
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=True))
    else:
        counts = result["counts"]
        print(f"Scope: {result['scope']}")
        print(f"Files: {counts['before']} -> {counts['after']}; "
              f"{counts['added']} added, {counts['removed']} removed, "
              f"{counts['changed']} changed, {counts['unchanged']} unchanged")
        sizes = result["bytes"]
        print(f"File bytes: {sizes['before']} -> {sizes['after']} ({sizes['delta']:+d})")
        for category in ("added", "removed", "changed"):
            print(f"\n{category.capitalize()} ({counts[category]}):")
            for item in result[category]:
                detail = (f"{item['before']['size_bytes']} -> {item['after']['size_bytes']} bytes"
                          if category == "changed" else f"{item['size_bytes']} bytes")
                print(f"  {json.dumps(item['path'], ensure_ascii=True)} ({detail})")
            if result["omitted"][category]:
                print(f"  ... {result['omitted'][category]} more; increase --limit or narrow --prefix")
    return 0


if __name__ == "__main__":
    sys.exit(main())
