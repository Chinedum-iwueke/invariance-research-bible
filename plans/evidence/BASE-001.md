<a id="base-001-evidence"></a>
# BASE-001 Completion Evidence

**Task:** Machine-verifiable implementation baseline
**Status:** Completed locally; CI evidence collection configured
**Validation date:** 2026-08-10

## Delivered contract

`implementation-baseline-v1` is implemented identically in the control-plane and Bulletproof repositories. Each repository now contains:

- a strict Draft 2020-12 JSON Schema;
- a repository-native, standard-library collector and validator;
- a clean-worktree guard with explicit `--allow-dirty` audit mode;
- sanitized Git identity and origin metadata;
- fixed runtime-version probes;
- tracked dependency-manifest, lock-file, and schema inventories with hashes;
- declared acceptance commands as argument arrays;
- the controlled ten-value claim vocabulary;
- explicit negative assertions for environment, ignored-file, raw-data, and remote-credential collection;
- private mode-0600 evidence output; and
- CI collection, independent schema validation, and 30-day artifact retention.

The collector is read-only with respect to repositories. It does not execute the declared acceptance commands, enumerate ignored files, read environment values, or inspect the Bulletproof data lake.

## Implementation pins

| Repository | Branch | Commit |
|---|---|---|
| Hermes Swarm Control Plane | `feat/base-001-implementation-baseline` | `92e01fb70441e31b753e606636f13acb3d8d3351` |
| Bulletproof BT | `feat/base-001-implementation-baseline` | `5a70e9857b2ec617b794fc1661f91dbd8a148da9` |

The pre-existing control-plane `.gitignore` modification and Bulletproof `src/bt/research_data/jobs/materialize.py` modification were not staged or changed.

## Acceptance evidence

| Check | Result |
|---|---|
| Control-plane BASE-001 fixtures | 8 passed |
| Bulletproof BASE-001 fixtures | 8 passed |
| Collector and schema byte compatibility | Exact match |
| Ruff on both implementations/tests | Passed |
| Python compilation | Passed |
| JSON Schema metaschema validation | Passed for both copies |
| Independent schema validation of emitted evidence | Passed for both repositories |
| Repeated collection | Byte-identical within each unchanged repository state |
| Default dirty guard | Exit 2 in both pre-existing dirty worktrees |
| Output permissions | Mode 0600 |
| Secret/raw-data scan | No credential, secret value, ignored data, or raw dataset entered evidence or commits |

Audit-mode evidence digests after the implementation commits were:

- control plane: `47e834e5a1f097ea72b45035987218a9ac1470728c187869db2e8110cf5a9f54`;
- Bulletproof: `88bf57e023f148ef2902880235e02bc7d56a3d64fba9ca6edc5417e71bc8c076`.

These digests explicitly record the unrelated dirty paths and are not release-quality clean-tree attestations. CI creates the clean-checkout evidence for each pushed commit.

## Inherited failures retained

The complete control-plane worker suite produced 175 passes and 10 failures. A detached worktree at the untouched base commit reproduced the same failure families (11 failures, 25 passes in the two selected modules): code-validation subprocess fixtures and PostgreSQL preflight fixtures disagree with the current environment/TLS contract. BASE-001 did not alter those surfaces.

The expanded Bulletproof slice produced 57 passes and one failure. The deterministic end-to-end artifact test also failed at the untouched `ba2a031...` pin, demonstrating inherited byte-level nondeterminism in `performance.json`. It remains a BT-001 defect and is not concealed by the successful BASE-001 fixtures.

## Completion decision

BASE-001 is complete because clean/dirty/missing-lock fixture repositories are covered, the evidence contract is strict and independently schema-valid, unchanged collection is stable, CI retains clean evidence, and sensitive or raw material is excluded. It does not claim that the repositories' declared test commands all pass. That broader closure belongs to BT-001 and the corresponding control-plane defect work.
