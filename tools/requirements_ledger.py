#!/usr/bin/env python3
"""Build and validate the machine-verifiable Bible requirement ledger."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "bible-requirement-ledger-v1.0.0"
REPORT_VERSION = "bible-requirement-coverage-v1.0.0"
REQUIREMENT_ID_RE = re.compile(r"^B(?:0[1-9]|10)-(?:CH\d{2}|APP-[A-Z])-R-[A-F0-9]{12}$")
PACKAGE_ID_RE = re.compile(
    r"\b(?:BASE|RI|GOV|CAD|AGT|LLM|DATA|BT|DISC|SHADOW|ML|RL|PORT|"
    r"RISK|EXEC|UI|CHAN|OPS|PLAT|SEC|WS|DEMO|LIVE|EVOLVE)-\d{3}\b"
)
NORMATIVE_RE = re.compile(
    r"\b(?:must|requires?|required|cannot|may not|never|only|prohibited|"
    r"does not|accepted when|acceptance|non-goals?|invariant|shall|is responsible for|"
    r"is accountable for|is authorized to|is not authorized to)\b",
    re.IGNORECASE,
)
SECTION_RE = re.compile(
    r"\b(?:acceptance|completion|requirement|contract|non-goal|invariant|"
    r"authority|security|recovery|definition of done|unsafe-use)\b",
    re.IGNORECASE,
)
RULE_RE = re.compile(r"^>\s*\*\*.*?(?:rule|invariant).*?\*\*", re.IGNORECASE)

ACCOUNTABLE_OWNERS = {
    1: "constitutional-governance",
    2: "hermes-governance",
    3: "knowledge-stewardship",
    4: "research-discovery",
    5: "bulletproof-laboratory",
    6: "ml-and-statistical-review",
    7: "portfolio-and-risk",
    8: "execution-and-production-risk",
    9: "agent-architecture-and-security",
    10: "architecture-and-platform-engineering",
}
BASELINE_REVIEW_DATE = "2026-08-10"
TOP_LEVEL_KEYS = {
    "schema_version",
    "generated_from",
    "claim_boundary",
    "source_inventory",
    "requirements",
}
INVENTORY_KEYS = {"path", "book", "locator", "content_sha256"}
REQUIREMENT_KEYS = {
    "requirement_id",
    "source",
    "statement",
    "kind",
    "normative_strength",
    "accountable_owner",
    "work_packages",
    "verification_methods",
    "disposition",
    "evidence_refs",
    "deferral",
    "depends_on",
    "review",
}
SOURCE_KEYS = {"path", "book", "locator", "heading", "line_hint", "statement_sha256"}
REVIEW_KEYS = {"status", "reviewed_by", "reviewed_on", "basis"}
REQUIREMENT_KINDS = {
    "acceptance",
    "authority",
    "contract",
    "invariant",
    "non_goal",
    "recovery",
    "requirement",
    "rule",
    "security",
}
NORMATIVE_STRENGTHS = {
    "acceptance_gate",
    "constitutional",
    "mandatory",
    "prohibited",
    "scope_boundary",
    "target",
}

# Chapter-level ownership is the reviewed traceability baseline in
# plans/BIBLE_CAPABILITY_COVERAGE.md. It is deliberately conservative: a requirement
# may map to several packages until BASE-003 evidence is refined by its domain owner.
BOOK_PACKAGE_RULES: dict[int, list[tuple[range, tuple[str, ...]]]] = {
    1: [
        (range(1, 6), ("GOV-001", "GOV-004", "RI-001", "RI-004", "RI-010", "CAD-002")),
        (range(6, 10), ("DISC-002", "DISC-003", "DISC-006", "DISC-007", "BT-002", "BT-006", "BT-007", "RI-008")),
        (range(10, 13), ("PORT-001", "PORT-002", "PORT-003", "PORT-004", "ML-002", "ML-003", "ML-004", "RISK-001", "RISK-002", "RISK-003")),
        (range(13, 17), ("RI-010", "CAD-002", "EVOLVE-001", "EVOLVE-002", "BASE-001", "BASE-002", "BASE-003")),
    ],
    2: [
        (range(1, 6), ("GOV-001", "GOV-002", "GOV-004", "AGT-001", "AGT-006", "PLAT-002")),
        (range(6, 11), ("DISC-001", "DISC-008", "DISC-009", "BT-006", "GOV-002", "GOV-003", "RISK-004")),
        (range(11, 18), ("AGT-002", "AGT-003", "AGT-004", "AGT-005", "AGT-006", "AGT-007", "AGT-008", "RI-011", "OPS-001", "OPS-002", "CHAN-001", "UI-001", "UI-002", "UI-004", "WS-001", "WS-002", "CAD-001", "CAD-002")),
    ],
    3: [
        (range(1, 6), ("RI-001", "RI-004", "RI-007", "RI-010", "BASE-002")),
        (range(6, 9), ("RI-002", "RI-007", "RI-009", "RI-012")),
        (range(9, 12), ("RI-003", "RI-004", "RI-011", "UI-003")),
        (range(12, 17), ("RI-008", "RI-010", "AGT-002", "BT-008")),
        (range(17, 19), ("RI-005", "RI-006", "RI-009", "RI-011", "SEC-001", "PLAT-005", "PLAT-007")),
    ],
    4: [
        (range(1, 6), ("DISC-002", "DISC-003", "DISC-006", "DISC-009")),
        (range(6, 12), ("DISC-003", "DISC-004", "DISC-005", "DISC-006", "AGT-004", "LLM-001")),
        (range(12, 18), ("DISC-007", "DISC-008", "DISC-009", "BT-006", "GOV-003")),
    ],
    5: [
        (range(1, 9), ("BT-001", "BT-002", "BT-004", "BT-005", "DATA-001", "DATA-002", "DATA-003")),
        (range(9, 16), ("BT-003", "BT-006", "BT-007", "BT-008", "BT-009", "RI-001", "RI-004")),
        (range(16, 18), ("SHADOW-001", "SHADOW-002", "BT-001", "BT-002", "DATA-003")),
    ],
    6: [
        (range(1, 8), ("ML-001", "ML-002", "ML-003", "BT-007")),
        (range(8, 13), ("ML-004", "ML-005", "ML-006", "RI-004")),
        (range(13, 17), ("RL-001", "RL-002", "RL-003", "ML-006", "RISK-005")),
    ],
    7: [
        (range(1, 8), ("PORT-001", "PORT-002", "PORT-003", "PORT-004", "RISK-001")),
        (range(8, 13), ("RISK-001", "RISK-002", "RISK-003", "RISK-005")),
        (range(13, 16), ("RISK-004", "RISK-005", "LIVE-001", "LIVE-002")),
    ],
    8: [
        (range(1, 7), ("EXEC-001", "EXEC-002", "EXEC-003", "DATA-001", "DATA-002")),
        (range(7, 13), ("EXEC-004", "EXEC-005", "EXEC-006", "EXEC-008", "SHADOW-001", "DEMO-001")),
        (range(13, 17), ("EXEC-007", "EXEC-009", "EXEC-010", "LIVE-001", "LIVE-002")),
    ],
    9: [
        (range(1, 10), ("AGT-001", "AGT-006", "AGT-007", "PLAT-002", "GOV-001")),
        (range(10, 15), ("AGT-002", "AGT-003", "AGT-004", "AGT-005", "RI-008", "SEC-001")),
        (range(15, 18), ("AGT-007", "AGT-008", "PLAT-004", "PLAT-005", "UI-001", "UI-002", "UI-006", "EVOLVE-001", "EVOLVE-002")),
    ],
    10: [
        (range(1, 8), ("BASE-001", "BASE-002", "BASE-003", "PLAT-001", "PLAT-003", "DATA-001", "DATA-002", "DATA-003", "RI-007")),
        (range(8, 14), ("RI-001", "RI-002", "RI-003", "RI-004", "RI-005", "RI-006", "RI-007", "RI-008", "RI-009", "RI-010", "RI-011", "RI-012", "BT-001", "BT-002", "BT-003", "BT-004", "BT-005", "BT-006", "BT-007", "BT-008", "BT-009", "SHADOW-001", "PORT-001", "RISK-001", "EXEC-001", "LIVE-001")),
        (range(14, 21), ("BASE-003", "OPS-003", "OPS-004", "OPS-005", "PLAT-002", "PLAT-003", "PLAT-004", "PLAT-005", "PLAT-006", "PLAT-007", "PLAT-008", "PLAT-009", "SEC-001", "SEC-002", "UI-005", "UI-006", "WS-001", "WS-002", "EVOLVE-001", "EVOLVE-002")),
    ],
}


@dataclass(frozen=True)
class SourceInfo:
    path: Path
    relative_path: str
    book: int
    locator: str
    chapter: int | None


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def canonical_json(value: Any) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n"


def normalize_markdown(value: str) -> str:
    value = re.sub(r"<!--.*?-->", "", value, flags=re.DOTALL)
    value = re.sub(r"<a\s+id=\"[^\"]+\"></a>", "", value)
    return re.sub(r"\s+", " ", value).strip()


def authority_sources(root: Path) -> list[SourceInfo]:
    """Return only the ten constitutional books that define authority.

    Book XI is a living, descriptive implementation record. Excluding it prevents an
    observed implementation detail from silently becoming institutional authority.
    """

    sources: list[SourceInfo] = []
    for path in sorted((root / "books").glob("book-*/chapters/*.md")):
        book = int(re.search(r"book-(\d+)", str(path)).group(1))  # type: ignore[union-attr]
        if book not in BOOK_PACKAGE_RULES:
            continue
        chapter = int(path.name.split("-", 1)[0])
        sources.append(SourceInfo(path, path.relative_to(root).as_posix(), book, f"CH{chapter:02d}", chapter))
    for path in sorted((root / "books").glob("book-*/appendices/*.md")):
        book = int(re.search(r"book-(\d+)", str(path)).group(1))  # type: ignore[union-attr]
        if book not in BOOK_PACKAGE_RULES:
            continue
        letter = path.name.split("-", 1)[0].upper()
        sources.append(SourceInfo(path, path.relative_to(root).as_posix(), book, f"APP-{letter}", None))
    return sources


def packages_for(source: SourceInfo) -> list[str]:
    rules = BOOK_PACKAGE_RULES[source.book]
    if source.chapter is None:
        return sorted({package for _, packages in rules for package in packages})
    for chapters, packages in rules:
        if source.chapter in chapters:
            return list(packages)
    raise ValueError(f"No package mapping for {source.relative_path}")


def blocks_with_context(text: str) -> Iterable[tuple[str, str, int, bool]]:
    """Yield normalized blocks as (heading, text, line, is_rule)."""

    lines = text.splitlines()
    heading = "document"
    paragraph: list[str] = []
    start_line = 1

    def flush() -> tuple[str, str, int, bool] | None:
        nonlocal paragraph
        if not paragraph:
            return None
        raw = "\n".join(paragraph)
        paragraph = []
        normalized = normalize_markdown(raw)
        if not normalized:
            return None
        return heading, normalized, start_line, bool(RULE_RE.match(raw))

    table_header_lines = {
        index + 1
        for index, line in enumerate(lines[:-1])
        if line.lstrip().startswith("|")
        and re.fullmatch(r"\|?\s*[-:| ]+\|?", lines[index + 1].strip())
    }
    for number, line in enumerate(lines, 1):
        if line.startswith("#"):
            item = flush()
            if item:
                yield item
            heading = normalize_markdown(line.lstrip("# "))
            continue
        if not line.strip():
            item = flush()
            if item:
                yield item
            continue
        if number in table_header_lines or re.fullmatch(r"\|?\s*[-:| ]+\|?", line.strip()):
            item = flush()
            if item:
                yield item
            continue
        if not paragraph:
            start_line = number
        # Keep rule continuation lines in the same block. Ordinary list/table lines
        # are independent requirements so one row cannot hide another.
        if paragraph and (line.startswith(("- ", "|")) or paragraph[0].startswith(("- ", "|"))):
            item = flush()
            if item:
                yield item
            start_line = number
        paragraph.append(line)
    item = flush()
    if item:
        yield item


def classify(statement: str, heading: str, is_rule: bool, appendix: bool) -> str:
    lowered = f"{heading} {statement}".lower()
    if "non-goal" in lowered or "non goal" in lowered:
        return "non_goal"
    if "acceptance" in lowered or "accepted when" in lowered or "definition of done" in lowered:
        return "acceptance"
    if is_rule:
        return "invariant" if "invariant" in lowered else "rule"
    if "invariant" in lowered:
        return "invariant"
    if any(word in lowered for word in ("authority", "authorized", "approval", "veto", "capital allocation")):
        return "authority"
    if any(word in lowered for word in ("security", "secret", "access", "protected evidence", "credential")):
        return "security"
    if any(word in lowered for word in ("rollback", "restore", "recovery", "reconcile")):
        return "recovery"
    if appendix or "contract" in lowered:
        return "contract"
    return "requirement"


def strength(statement: str, kind: str) -> str:
    lowered = statement.lower()
    if re.search(r"\b(?:may not|cannot|never|prohibited)\b", lowered):
        return "prohibited"
    if re.search(r"\b(?:must|required|requires|shall)\b", lowered):
        return "mandatory"
    if kind in {"rule", "invariant", "authority"}:
        return "constitutional"
    if kind == "acceptance":
        return "acceptance_gate"
    if kind == "non_goal":
        return "scope_boundary"
    return "target"


def verification_for(kind: str) -> list[str]:
    base = ["contract_test", "integration_test", "evidence_dossier"]
    if kind in {"authority", "security", "non_goal"}:
        base.extend(["authorization_test", "adversarial_test"])
    if kind == "recovery":
        base.extend(["failure_injection", "recovery_rehearsal"])
    if kind == "acceptance":
        base.append("intended_environment_acceptance")
    return sorted(set(base))


def should_capture(statement: str, heading: str, is_rule: bool, appendix: bool) -> bool:
    if heading.strip().lower() == "source note":
        return False
    if statement.startswith("#") or re.fullmatch(r"\|?\s*[-:| ]+\|?", statement):
        return False
    if is_rule or appendix or SECTION_RE.search(heading):
        return True
    return bool(NORMATIVE_RE.search(statement))


def extract_requirements(root: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    requirements: list[dict[str, Any]] = []
    inventory: list[dict[str, Any]] = []
    for source in authority_sources(root):
        raw = source.path.read_text(encoding="utf-8")
        inventory.append(
            {
                "path": source.relative_path,
                "book": source.book,
                "locator": source.locator,
                "content_sha256": sha256_text(raw),
            }
        )
        for heading, statement, line, is_rule in blocks_with_context(raw):
            appendix = source.chapter is None
            if not should_capture(statement, heading, is_rule, appendix):
                continue
            statement_digest = sha256_text(statement)
            identity_digest = sha256_text(f"{source.relative_path}\n{statement}")
            requirement_id = f"B{source.book:02d}-{source.locator}-R-{identity_digest[:12].upper()}"
            kind = classify(statement, heading, is_rule, appendix)
            requirements.append(
                {
                    "requirement_id": requirement_id,
                    "source": {
                        "path": source.relative_path,
                        "book": source.book,
                        "locator": source.locator,
                        "heading": heading,
                        "line_hint": line,
                        "statement_sha256": statement_digest,
                    },
                    "statement": statement,
                    "kind": kind,
                    "normative_strength": strength(statement, kind),
                    "accountable_owner": ACCOUNTABLE_OWNERS[source.book],
                    "work_packages": packages_for(source),
                    "verification_methods": verification_for(kind),
                    "disposition": "planned",
                    "evidence_refs": [],
                    "deferral": None,
                    "depends_on": [],
                    "review": {
                        "status": "reviewed",
                        "reviewed_by": "codex-base-003-implementation-audit",
                        "reviewed_on": BASELINE_REVIEW_DATE,
                        "basis": (
                            "Machine-assisted exact-text classification and chapter-level "
                            "ownership mapping; domain review is required before an "
                            "implementation disposition changes."
                        ),
                    },
                }
            )
    requirements.sort(key=lambda item: item["requirement_id"])
    return inventory, requirements


def build_ledger(root: Path) -> dict[str, Any]:
    inventory, requirements = extract_requirements(root)
    return {
        "schema_version": SCHEMA_VERSION,
        "generated_from": "books/book-*/chapters/*.md and books/book-*/appendices/*.md",
        "claim_boundary": (
            "Complete disposition proves planning coverage, not implementation, "
            "operational qualification, scientific truth, or profitability."
        ),
        "source_inventory": inventory,
        "requirements": requirements,
    }


def known_packages(root: Path) -> set[str]:
    texts = [
        (root / "plans" / "CODEX_IMPLEMENTATION_BACKLOG.md").read_text(encoding="utf-8"),
        (root / "plans" / "BIBLE_CAPABILITY_COVERAGE.md").read_text(encoding="utf-8"),
    ]
    return set(PACKAGE_ID_RE.findall("\n".join(texts)))


def validate_ledger(ledger: dict[str, Any], root: Path) -> list[str]:
    errors: list[str] = []
    unknown_top_level = sorted(set(ledger) - TOP_LEVEL_KEYS)
    missing_top_level = sorted(TOP_LEVEL_KEYS - set(ledger))
    if unknown_top_level:
        errors.append(f"ledger has unknown fields: {unknown_top_level}")
    if missing_top_level:
        errors.append(f"ledger is missing fields: {missing_top_level}")
    if ledger.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION}")

    expected_inventory, extracted = extract_requirements(root)
    expected_by_id = {item["requirement_id"]: item for item in extracted}
    expected_sources = {item["path"] for item in expected_inventory}
    inventory = ledger.get("source_inventory")
    requirements = ledger.get("requirements")
    if not isinstance(inventory, list):
        errors.append("source_inventory must be a list")
        inventory = []
    if not isinstance(requirements, list):
        errors.append("requirements must be a list")
        requirements = []

    inventory_by_path = {
        item.get("path"): item for item in inventory if isinstance(item, dict)
    }
    for index, item in enumerate(inventory):
        if isinstance(item, dict):
            unknown = sorted(set(item) - INVENTORY_KEYS)
            missing = sorted(INVENTORY_KEYS - set(item))
            if unknown:
                errors.append(f"source_inventory[{index}] has unknown fields: {unknown}")
            if missing:
                errors.append(f"source_inventory[{index}] is missing fields: {missing}")
    inventory_paths = set(inventory_by_path)
    expected_inventory_by_path = {item["path"]: item for item in expected_inventory}
    missing_sources = sorted(expected_sources - inventory_paths)
    extra_sources = sorted(inventory_paths - expected_sources)
    if missing_sources:
        errors.append(f"source inventory is missing: {missing_sources}")
    if extra_sources:
        errors.append(f"source inventory has unknown paths: {extra_sources}")
    for path in sorted(expected_sources & inventory_paths):
        if inventory_by_path[path] != expected_inventory_by_path[path]:
            errors.append(f"source inventory digest or identity is stale: {path}")

    ids: list[str] = []
    packages = known_packages(root)
    dependency_graph: dict[str, list[str]] = {}
    record_by_id: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(requirements):
        prefix = f"requirements[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        unknown_fields = sorted(set(item) - REQUIREMENT_KEYS)
        missing_fields = sorted(REQUIREMENT_KEYS - set(item))
        if unknown_fields:
            errors.append(f"{prefix} has unknown fields: {unknown_fields}")
        if missing_fields:
            errors.append(f"{prefix} is missing fields: {missing_fields}")
        requirement_id = item.get("requirement_id")
        if not isinstance(requirement_id, str) or not REQUIREMENT_ID_RE.fullmatch(requirement_id):
            errors.append(f"{prefix}.requirement_id is invalid")
            continue
        ids.append(requirement_id)
        record_by_id[requirement_id] = item
        dependency_graph[requirement_id] = item.get("depends_on", [])

        source = item.get("source", {})
        if not isinstance(source, dict):
            errors.append(f"{requirement_id}: source must be an object")
            source = {}
        else:
            unknown = sorted(set(source) - SOURCE_KEYS)
            missing = sorted(SOURCE_KEYS - set(source))
            if unknown:
                errors.append(f"{requirement_id}: source has unknown fields {unknown}")
            if missing:
                errors.append(f"{requirement_id}: source is missing fields {missing}")
        statement = item.get("statement")
        if not isinstance(statement, str) or not statement.strip():
            errors.append(f"{requirement_id}: statement must be non-empty")
            continue
        if source.get("statement_sha256") != sha256_text(statement):
            errors.append(f"{requirement_id}: stale statement digest")
        identity_input = f"{source.get('path')}\n{statement}"
        expected_identity = sha256_text(identity_input)[:12].upper()
        expected_id = (
            f"B{source.get('book', 0):02d}-{source.get('locator')}"
            f"-R-{expected_identity}"
        )
        if requirement_id != expected_id:
            errors.append(f"{requirement_id}: identity does not match source and statement")
        expected = expected_by_id.get(requirement_id)
        if expected is None:
            errors.append(f"{requirement_id}: source statement is stale, removed, or not normative")
        elif expected["statement"] != statement:
            errors.append(f"{requirement_id}: statement differs from canonical source")

        work_packages = item.get("work_packages")
        if not isinstance(work_packages, list) or not work_packages:
            errors.append(f"{requirement_id}: at least one work package is required")
        else:
            unknown = sorted(set(work_packages) - packages)
            if unknown:
                errors.append(f"{requirement_id}: unknown work packages {unknown}")
        if not item.get("accountable_owner"):
            errors.append(f"{requirement_id}: accountable_owner is required")
        if not item.get("verification_methods"):
            errors.append(f"{requirement_id}: verification_methods are required")
        if item.get("kind") not in REQUIREMENT_KINDS:
            errors.append(f"{requirement_id}: invalid kind {item.get('kind')!r}")
        if item.get("normative_strength") not in NORMATIVE_STRENGTHS:
            errors.append(
                f"{requirement_id}: invalid normative_strength "
                f"{item.get('normative_strength')!r}"
            )

        disposition = item.get("disposition")
        if disposition not in {"planned", "implemented", "deferred", "not_applicable"}:
            errors.append(f"{requirement_id}: invalid disposition {disposition!r}")
        evidence_refs = item.get("evidence_refs")
        if not isinstance(evidence_refs, list):
            errors.append(f"{requirement_id}: evidence_refs must be a list")
            evidence_refs = []
        if disposition == "implemented" and not evidence_refs:
            errors.append(f"{requirement_id}: implemented disposition requires evidence")
        for evidence_ref in evidence_refs:
            if not isinstance(evidence_ref, str) or not (root / evidence_ref).exists():
                errors.append(f"{requirement_id}: evidence does not exist: {evidence_ref!r}")
        if disposition in {"deferred", "not_applicable"} and not item.get("deferral"):
            errors.append(f"{requirement_id}: {disposition} disposition requires rationale")
        review = item.get("review", {})
        if not isinstance(review, dict):
            errors.append(f"{requirement_id}: review must be an object")
            review = {}
        else:
            unknown = sorted(set(review) - REVIEW_KEYS)
            missing = sorted(REVIEW_KEYS - set(review))
            if unknown:
                errors.append(f"{requirement_id}: review has unknown fields {unknown}")
            if missing:
                errors.append(f"{requirement_id}: review is missing fields {missing}")
        if review.get("status") != "reviewed" or not review.get("reviewed_by"):
            errors.append(f"{requirement_id}: reviewed disposition is required")

    duplicates = sorted(key for key, count in Counter(ids).items() if count > 1)
    if duplicates:
        errors.append(f"duplicate requirement IDs: {duplicates}")

    ledger_ids = set(ids)
    extracted_ids = set(expected_by_id)
    missing_requirements = sorted(extracted_ids - ledger_ids)
    if missing_requirements:
        errors.append(f"unmapped normative requirements: {missing_requirements}")
    unexpected_requirements = sorted(ledger_ids - extracted_ids)
    if unexpected_requirements:
        errors.append(f"ledger requirements absent from sources: {unexpected_requirements}")

    for requirement_id, dependencies in dependency_graph.items():
        if not isinstance(dependencies, list):
            errors.append(f"{requirement_id}: depends_on must be a list")
            continue
        unknown = sorted(set(dependencies) - ledger_ids)
        if unknown:
            errors.append(f"{requirement_id}: unknown dependencies {unknown}")

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, path: list[str]) -> None:
        if node in visiting:
            errors.append(f"circular requirement dependency: {' -> '.join(path + [node])}")
            return
        if node in visited:
            return
        visiting.add(node)
        for dependency in dependency_graph.get(node, []):
            if dependency in dependency_graph:
                visit(dependency, path + [node])
        visiting.remove(node)
        visited.add(node)

    for requirement_id in dependency_graph:
        visit(requirement_id, [])

    covered_sources = {
        item.get("source", {}).get("path")
        for item in requirements
        if isinstance(item, dict)
    }
    source_without_requirement = sorted(expected_sources - covered_sources)
    if source_without_requirement:
        errors.append(f"authority sources without requirements: {source_without_requirement}")
    used_packages = {
        package
        for item in requirements
        if isinstance(item, dict)
        for package in item.get("work_packages", [])
    }
    orphan_packages = sorted(packages - used_packages)
    if orphan_packages:
        errors.append(f"work packages without requirements: {orphan_packages}")
    return errors


def coverage_report(ledger: dict[str, Any], root: Path) -> dict[str, Any]:
    requirements = ledger["requirements"]
    by_book: dict[str, int] = defaultdict(int)
    by_kind: dict[str, int] = defaultdict(int)
    by_disposition: dict[str, int] = defaultdict(int)
    by_package: dict[str, int] = defaultdict(int)
    reviewed = 0
    for item in requirements:
        by_book[f"book-{item['source']['book']:02d}"] += 1
        by_kind[item["kind"]] += 1
        by_disposition[item["disposition"]] += 1
        reviewed += item["review"]["status"] == "reviewed"
        for package in item["work_packages"]:
            by_package[package] += 1
    ledger_digest = sha256_text(canonical_json(ledger))
    all_packages = known_packages(root)
    used_packages = set(by_package)
    return {
        "schema_version": REPORT_VERSION,
        "ledger_sha256": ledger_digest,
        "source_file_count": len(ledger["source_inventory"]),
        "requirement_count": len(requirements),
        "reviewed_count": reviewed,
        "unreviewed_count": len(requirements) - reviewed,
        "orphan_requirement_count": sum(not item["work_packages"] for item in requirements),
        "orphan_work_package_count": len(all_packages - used_packages),
        "by_book": dict(sorted(by_book.items())),
        "by_kind": dict(sorted(by_kind.items())),
        "by_disposition": dict(sorted(by_disposition.items())),
        "by_work_package": dict(sorted(by_package.items())),
        "claim_boundary": ledger["claim_boundary"],
    }


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(canonical_json(value), encoding="utf-8")


def command_build(root: Path, ledger_path: Path, report_path: Path) -> int:
    ledger = build_ledger(root)
    errors = validate_ledger(ledger, root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    write_json(ledger_path, ledger)
    write_json(report_path, coverage_report(ledger, root))
    print(
        f"Built {len(ledger['requirements'])} reviewed requirements from "
        f"{len(ledger['source_inventory'])} authority files."
    )
    return 0


def command_validate(root: Path, ledger_path: Path, report_path: Path) -> int:
    ledger = load_json(ledger_path)
    errors = validate_ledger(ledger, root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    expected_report = coverage_report(ledger, root)
    if not report_path.exists():
        print(f"ERROR: coverage report is missing: {report_path}", file=sys.stderr)
        return 1
    actual_report = load_json(report_path)
    if actual_report != expected_report:
        print("ERROR: coverage report is stale; run the build command", file=sys.stderr)
        return 1
    print(
        f"Validated {len(ledger['requirements'])} requirements, "
        f"{len(ledger['source_inventory'])} sources, zero orphans, and a current report."
    )
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("build", "validate"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--ledger", type=Path)
    parser.add_argument("--report", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    ledger_path = args.ledger or root / "requirements" / "ledger.json"
    report_path = args.report or root / "requirements" / "coverage-report.json"
    if args.command == "build":
        return command_build(root, ledger_path, report_path)
    return command_validate(root, ledger_path, report_path)


if __name__ == "__main__":
    raise SystemExit(main())
