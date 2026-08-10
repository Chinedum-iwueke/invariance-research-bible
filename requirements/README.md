# Bible Requirement Ledger

`ledger.json` is the canonical, reviewed planning-disposition ledger for normative
statements in all 169 chapters and 31 appendices of the ten-volume Bible.
`coverage-report.json` is a disposable projection derived from that ledger.

The ledger proves that each captured requirement has:

- a stable source-derived requirement ID;
- exact source text and a statement digest;
- an accountable institutional owner;
- at least one known engineering work package;
- declared verification methods;
- an implementation disposition;
- evidence for any `implemented` claim or rationale for a deferral; and
- a reviewed extraction/ownership decision.

It does **not** prove that planned requirements are implemented, that implemented
software is production-qualified, that a scientific claim is true, or that the firm is
profitable.

## Commands

Validate the checked-in ledger and derived report:

```bash
python3 tools/requirements_ledger.py validate
```

After an intentional Bible or ownership-map change, rebuild and inspect the diff:

```bash
python3 tools/requirements_ledger.py build
python3 tools/requirements_ledger.py validate
python3 -m unittest discover -s tests -p 'test_*.py'
```

Rebuilding is not approval. A reviewer must inspect added, removed, or changed exact
statements, owner/package mappings, dispositions, evidence references, and claim
boundaries before committing the regenerated files.

## Failure semantics

Validation fails closed for missing authority files, newly unmapped normative text,
stale source text/digests, duplicate or malformed IDs, unknown packages, missing
owners/verifications, nonexistent evidence, unsupported dispositions, unreviewed
records, circular dependencies, orphan requirements, and stale coverage reports.

Source line numbers are hints only. Identity is derived from source path and normalized
exact statement text, so moving text without changing it keeps its requirement identity;
changing the normative statement creates a new identity and requires review.
