from __future__ import annotations

import contextlib
import copy
import importlib.util
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "requirements_ledger", ROOT / "tools" / "requirements_ledger.py"
)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class RequirementLedgerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.ledger = json.loads((ROOT / "requirements" / "ledger.json").read_text())
        cls.report = json.loads(
            (ROOT / "requirements" / "coverage-report.json").read_text()
        )
        cls.mutations = json.loads(
            (
                ROOT
                / "tests"
                / "fixtures"
                / "requirements-ledger"
                / "mutations.json"
            ).read_text()
        )

    def assert_has_error(self, ledger: dict, fragment: str) -> None:
        errors = MODULE.validate_ledger(ledger, ROOT)
        self.assertTrue(
            any(fragment in error for error in errors),
            f"Expected {fragment!r} in errors: {errors[:8]}",
        )

    def test_checked_in_ledger_is_valid_and_deterministic(self) -> None:
        self.assertEqual([], MODULE.validate_ledger(self.ledger, ROOT))
        self.assertEqual(self.ledger, MODULE.build_ledger(ROOT))
        self.assertEqual(self.report, MODULE.coverage_report(self.ledger, ROOT))

    def test_every_authority_file_and_book_is_covered(self) -> None:
        inventory = self.ledger["source_inventory"]
        covered = {item["source"]["path"] for item in self.ledger["requirements"]}
        self.assertEqual(200, len(inventory))
        self.assertEqual({item["path"] for item in inventory}, covered)
        self.assertEqual(set(range(1, 11)), {item["book"] for item in inventory})
        self.assertEqual(169, sum("/chapters/" in item["path"] for item in inventory))
        self.assertEqual(31, sum("/appendices/" in item["path"] for item in inventory))

    def test_all_requirements_are_reviewed_owned_and_disposed(self) -> None:
        for item in self.ledger["requirements"]:
            self.assertEqual("reviewed", item["review"]["status"])
            self.assertTrue(item["accountable_owner"])
            self.assertTrue(item["work_packages"])
            self.assertTrue(item["verification_methods"])
            self.assertIn(
                item["disposition"],
                {"planned", "implemented", "deferred", "not_applicable"},
            )
        self.assertEqual(0, self.report["orphan_requirement_count"])
        self.assertEqual(0, self.report["orphan_work_package_count"])
        self.assertEqual(0, self.report["unreviewed_count"])

    def test_adversarial_mutation_fixtures_fail_closed(self) -> None:
        for fixture in self.mutations:
            with self.subTest(fixture=fixture["name"]):
                ledger = copy.deepcopy(self.ledger)
                first = ledger["requirements"][0]
                second = ledger["requirements"][1]
                name = fixture["name"]
                if name == "missing_source":
                    ledger["source_inventory"].pop()
                elif name == "unmapped_requirement":
                    ledger["requirements"].pop()
                elif name == "duplicate_id":
                    ledger["requirements"].append(copy.deepcopy(first))
                elif name == "unknown_package":
                    first["work_packages"] = ["NOT-A-REAL-PACKAGE-999"]
                elif name == "stale_digest":
                    first["source"]["statement_sha256"] = "0" * 64
                elif name == "stale_source_digest":
                    ledger["source_inventory"][0]["content_sha256"] = "0" * 64
                elif name == "false_completion":
                    first["disposition"] = "implemented"
                    first["evidence_refs"] = []
                elif name == "missing_evidence":
                    first["disposition"] = "implemented"
                    first["evidence_refs"] = ["plans/evidence/DOES-NOT-EXIST.md"]
                elif name == "circular_dependency":
                    first["depends_on"] = [second["requirement_id"]]
                    second["depends_on"] = [first["requirement_id"]]
                elif name == "unknown_top_level_field":
                    ledger["unexpected"] = True
                elif name == "unknown_nested_field":
                    first["source"]["unexpected"] = True
                else:
                    self.fail(f"Unknown mutation fixture: {name}")
                self.assert_has_error(ledger, fixture["expected_error"])

    def test_cli_validation_rejects_stale_coverage_report(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            directory_path = Path(directory)
            ledger_path = directory_path / "ledger.json"
            report_path = directory_path / "report.json"
            ledger_path.write_text(json.dumps(self.ledger))
            stale_report = copy.deepcopy(self.report)
            stale_report["requirement_count"] -= 1
            report_path.write_text(json.dumps(stale_report))
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                result = MODULE.command_validate(ROOT, ledger_path, report_path)
            self.assertEqual(1, result)
            self.assertIn("coverage report is stale", stderr.getvalue())

    def test_json_schema_contract_has_strict_top_level_and_requirement_objects(self) -> None:
        schema = json.loads(
            (ROOT / "requirements" / "ledger.schema.json").read_text()
        )
        self.assertFalse(schema["additionalProperties"])
        requirement = schema["$defs"]["requirement"]
        self.assertFalse(requirement["additionalProperties"])
        self.assertIn("requirement_id", requirement["required"])
        self.assertIn("work_packages", requirement["required"])
        self.assertIn("evidence_refs", requirement["required"])


if __name__ == "__main__":
    unittest.main()
