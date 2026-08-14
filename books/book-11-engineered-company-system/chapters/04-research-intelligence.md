<a id="research-intelligence-as-built"></a>
# 4. Research Intelligence

## 4.1 Purpose and non-authority

Research Intelligence is the institutional evidence and memory layer. PostgreSQL and
the object store hold canonical records; retrieval and graph tables are disposable
projections. RI can recover, classify, retrieve, compare, assemble and preserve
evidence. It cannot approve a hypothesis, start an experiment, promote a result or
allocate capital.

## 4.2 Ingestion pipeline

```mermaid
flowchart TD
    File[Founder inbox / approved upload / feed] --> Digest[SHA-256 and media validation]
    Digest --> Q[Content-addressed quarantine]
    Q --> Scan[Type, active-content, malware and injection gates]
    Scan --> Recover[Born-digital extraction or offline OCR]
    Recover --> Structure[Section, paragraph, table, figure, equation, citation recovery]
    Structure --> Validate[Coordinates, hierarchy, confidence and size validation]
    Validate -->|pass| Publish[Atomic canonical publication]
    Validate -->|fail| Remediate[Retained quarantine and remediation findings]
    Publish --> Source[Source]
    Source --> Edition[Edition]
    Edition --> Artifact[Artifact]
    Artifact --> Objects[Scientific objects]
    Objects --> Projections[Retrieval and graph rebuild]
```

Files are never executed. Archives, active PDF content, instruction-like text,
oversized payloads, malformed structures and low-confidence extraction are bounded or
rejected. Original artifacts are retained for exact coordinate replay. PR 33 adds
offline Tesseract/PDFium recovery and raises the bounded scientific-ingestion limit to
100 MiB. The settled 2026-08-14 founder-inbox ledger covers 120 files: 117 are usable
canonical or duplicate-backed evidence and three remain explicitly quarantined. Of the
last twelve exceptions, governed recovery safely resolved nine. One PDF is structurally
unreadable by both parsers; two extract successfully but contain instruction-like text
that cannot cross the current evidence trust boundary without explicit quoted-evidence
semantics. No scanner rule was weakened to improve the count.

The Research Ingestion Recovery Steward is a deterministic fixed-command service. It
claims bounded recovery work, preserves original evidence, creates inert recovered
editions, enforces attempt ceilings, reconciles the inbox, and rebuilds retrieval and
graph projections after a settled batch. Its source and tests exist; activation on VM2
is a separate privileged systemd installation and must be observed before it is called
active.

## 4.3 Canonical object kernel

Implemented object types are source, edition, artifact, scientific object, claim,
method, assumption, dataset, run, result, review, decision, belief and episode.
Identity includes canonical UUID, content version/digest, producer identity and aliases,
project, access class, authority class and typed payload. References become canonical
lineage edges. Immutable identity conflicts fail rather than overwrite history.

## 4.4 Retrieval

The `canonical-scientific` projection supports:

- exact UUID, digest, alias and exact-text matching;
- lexical term-frequency similarity;
- deterministic network-free hashed-vector similarity with a small declared synonym
  map;
- graph-assisted expansion over canonical neighbors;
- deterministic reciprocal-rank fusion (`rrf-v1`);
- project, scientific type, access class and schema compatibility filters;
- stale-corpus detection and fail-closed projection version checks;
- reauthorization against the canonical object before returning content;
- exact source-coordinate replay.

The vector channel is a reproducible baseline, not a learned domain embedding model.
Production relevance at full-corpus scale remains an evaluation obligation.

## 4.5 Institutional memory

RI-004 implements supporting and opposing evidence, comparability review, valid
negative results versus invalid attempts, belief revisions, episodes and immutable
frozen dossiers. A dossier binds its query, evidence identities, citations, opposing
evidence and digest. Protected evidence can be represented as redacted existence and
access reason without disclosing content.

Operational memory is separate. It records system observations and lifecycle actions
such as assign, defer, resolve and reopen. It does not execute the noted work.

## 4.6 Corpus operations and synchronization

RI-005 provides content-free security findings, aggregate metrics/SLO state,
digest-bound metadata backup, empty-target restore, stale queue repair and projection
rebuild. RI-007 adds a durable sync run and item ledger for:

- the founder's Mac inbox;
- legacy Hermes research records;
- `imported-prior-results`;
- a bounded Bulletproof research-memory export.

Each eligible item must end as canonical, quarantined, duplicate, superseded, excluded
or failed with a reason. Raw Bulletproof memory and its multi-gigabyte lake are not
copied into Hermes; only a bounded digest-bound projection is registered.

## 4.7 Surveillance

RI-006 has allowlisted HTTPS feeds, rights/access metadata, fetch success/failure
receipts, duplicate/correction/retraction history, abstract poisoning rejection,
corpus-grounded novelty, technique briefs, proposal-only routing and weekly digest
freezing. It does not auto-adopt a paper or auto-create a live research trial.

## 4.8 Typed knowledge graph and cognitive services

RI-008, implemented in PR 34 and deployed on VM2 at this snapshot, adds:

- allowlisted predicates: `derived_from`, `supersedes`, `supports`, `contradicts`,
  `uses_method`, `uses_dataset`, `produced_result`, `reviews`, `decides_on`,
  `belongs_to_trial_family`, `depends_on` and `cites`;
- endpoint-type direction validation;
- half-open validity intervals and explicit provenance objects;
- edge access classes that cannot underclassify protected endpoints/provenance;
- digest-bound projection manifests;
- bounded neighborhood, simple-path and subgraph traversal with cycle protection;
- access filtering before traversal and stale-projection failure;
- citation-bearing context packs;
- deterministic decimal mean, sample standard deviation, Sharpe and maximum drawdown;
- persisted idempotent receipts binding tool/version/input/output/context/actor;
- a canonical Mission Control graph explorer.

```mermaid
flowchart LR
    Source --> Edition --> Artifact --> ScientificObject
    ScientificObject -->|cites/supports/contradicts| Claim
    Claim -->|depends_on| Assumption
    Run -->|uses_method| Method
    Run -->|uses_dataset| Dataset
    Run -->|produced_result| Result
    Review -->|reviews| Result
    Decision -->|decides_on| Result
    Result -->|supports/contradicts| Claim
    Claim --> Belief
```

The graph is not a graph database source of truth. Canonical IDs and edges remain in
the evidence kernel; the graph projection can be dropped and deterministically rebuilt.

The live projection observed on 2026-08-14 contains 623,729 nodes and 1,097,688 edges
under manifest digest
`e44e13f0c955cddcd09f1cb5054914ace1e79f4514116b6f15ac0654028cfeb9`.
That observation proves migration and rebuild, not domain expertise. A retained live
citation/context replay and cognitive-tool receipt remain the final RI-008 acceptance
evidence at this point in the snapshot.

## 4.9 Readiness boundary

The inbox reconciliation and graph freeze gates for RI-009 are now satisfied. RI-009
must measure domain curricula, coverage, held-out retrieval, citation fidelity,
contradiction recall, calibration and abstention against versioned evaluation sets.
Upload count is not domain expertise, and the three retained quarantines are visible
coverage facts rather than silent omissions.

## 4.10 Domain curriculum and institutional-brain evaluation

RI-009 source at control-plane commit `e9b3db4` introduces a qualification layer above
the legacy domain profile. Each curriculum version binds to exact retrieval-corpus and
graph-manifest digests and declares:

- an acyclic ontology of topics and prerequisites;
- canonical evidence anchors and separate canonical source anchors, preventing many
  paragraphs from one book from masquerading as source diversity;
- required opposing evidence;
- allowed authority classes and a maximum quarantine fraction;
- qualified roles and a bounded review cadence.

Evaluation sets contain answerable, adversarial, cross-domain and mandatory abstention
cases. The service runs those cases through canonical hybrid retrieval and measures
retrieval recall, citation fidelity, opposing-evidence recall, abstention accuracy,
cross-domain leakage and topic coverage. Every threshold must pass. A changed corpus or
graph digest makes the qualification stale; source uploads do not silently preserve an
expertise claim.

The live RI-008 acceptance attempt also exposed a production-scale query defect: the
original traversal materialized all 623,729 node IDs into one PostgreSQL statement and
exceeded PostgreSQL's parameter ceiling. Commit `e9b3db4` replaces that path with
access-filtered bounded frontier traversal and caps graph overview queries. This fix is
tested but must be deployed and replayed before RI-008 or RI-009 is called fully live.
