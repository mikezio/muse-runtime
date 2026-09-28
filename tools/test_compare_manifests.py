"""Small fixtures for manifest parsing and comparison; no archive required."""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("compare-manifests.py")
SPEC = importlib.util.spec_from_file_location("compare_manifests", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def row(name, size=10, digest="a"):
    return f"{digest * 64}  {size}  {name}\n"


class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.before = Path(self.temp.name) / "before.txt"
        self.after = Path(self.temp.name) / "after.txt"

    def test_spaces_changes_and_bounded_json_cli(self):
        self.before.write_text(row("./opt/same") + row("./opt/changed file")
                               + row("./home/removed"))
        self.after.write_text(row("./opt/same") + row("./opt/changed file", 12, "b")
                              + row("./opt/added file") + row("./home/added"))
        run = subprocess.run([sys.executable, str(SCRIPT), str(self.before),
                              str(self.after), "--json", "--limit", "1"],
                             capture_output=True, text=True, check=True)
        result = json.loads(run.stdout)
        self.assertEqual(result["counts"], {"before": 3, "after": 4, "added": 2,
                                           "removed": 1, "changed": 1, "unchanged": 1})
        self.assertEqual(result["changed"][0]["path"], "opt/changed file")
        self.assertEqual(result["bytes"]["delta"], 12)
        self.assertEqual(result["omitted"]["added"], 1)

    def test_prefix_boundary_and_zero_limit(self):
        entries = {p: {"sha256": "a" * 64, "size_bytes": 5}
                   for p in ("opt/skills/a", "opt/skills extra/b")}
        result = MODULE.compare({}, entries, limit=0, prefix="./opt/skills/")
        self.assertEqual(result["counts"]["added"], 1)
        self.assertEqual(result["added"], [])
        self.assertEqual(result["omitted"]["added"], 1)

    def test_malformed_and_unsafe_records(self):
        for value in ("broken\n", row("/absolute"), row("./opt/../home/a"),
                      row("./opt//a"), row("./opt/a\tbad"), row("./opt/a\\b"),
                      row("./opt/a", -1), row("./opt/a", digest="z"),
                      row("./opt/a") + row("opt/a")):
            with self.subTest(value=value):
                self.before.write_text(value)
                with self.assertRaises(ValueError):
                    MODULE.read_manifest(self.before)

    def test_malformed_cli_exits_two_without_traceback(self):
        self.before.write_text("invalid\n")
        self.after.write_text("")
        run = subprocess.run([sys.executable, str(SCRIPT), str(self.before), str(self.after)],
                             capture_output=True, text=True)
        self.assertEqual(run.returncode, 2)
        self.assertIn(":1: expected", run.stderr)
        self.assertNotIn("Traceback", run.stderr)

    def test_same_hash_different_size_counts_changed(self):
        before = {"opt/a": {"sha256": "a" * 64, "size_bytes": 1}}
        after = {"opt/a": {"sha256": "a" * 64, "size_bytes": 2}}
        self.assertEqual(MODULE.compare(before, after)["counts"]["changed"], 1)


if __name__ == "__main__":
    unittest.main()
