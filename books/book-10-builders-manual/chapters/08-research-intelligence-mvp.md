<a id="b10-c08"></a>
# Chapter 8 — Research Intelligence MVP

The MVP makes institutional evidence retrievable, attributable, and comparable before adding elaborate graphs or autonomous curation.

## 8.1 Minimum slice

Ingest sources and run bundles; register identities and schemas; extract claims with source links; store evidence and decisions; search metadata and full text; retrieve compatible experiments; and show lineage and access status.

## 8.2 Canonical core

Source, artifact, claim, evidence relation, question, hypothesis, experiment, run, decision, and belief records live in transactional and object stores. Search and graph projections rebuild from them.

## 8.3 Curation

Agents propose extraction and links. Validators and reviewers publish material records. Contradictions coexist. Unknown compatibility prevents aggregation.

## 8.4 Acceptance

Given a claim, retrieve primary sources, supporting and opposing evidence, producer versions, experiments, decisions, and limitations. Given a run, trace back to question and forward to decisions.

## 8.5 Journal-surveillance extension

After the canonical ingestion slice is reliable, add a literature-surveillance service with:

- an approved source and journal registry containing scope, identifiers, authority class, rights, connector, owner, cadence, freshness objective, and enabled state;
- a scheduler for daily and weekly acquisition jobs with idempotent cursors, retry bounds, backoff, cost budgets, and missed-run recovery;
- feed, metadata, DOI, issue, abstract, and rights-permitted full-text adapters isolated behind versioned read-only interfaces;
- immutable acquisition manifests recording the expected source set, observed arrivals, queries, timestamps, response identity, digests, failures, and coverage gaps;
- work, edition, and artifact reconciliation before recovery, plus correction, retraction, duplicate, and citation-chain handling;
- a bounded knowledge-agent pipeline that creates cited digests, claim and method extractions, nearest-prior comparisons, contradiction alerts, applicability notes, and technique proposals;
- a triage queue that routes proposals to the accountable Book IV–VIII workflow and records dismiss, watch, investigate, register, experiment, adopt, or retire dispositions with reasons; and
- dashboards and alerts for feed health, freshness, coverage, rights failures, recovery quality, backlog, routing latency, and sampled miss and false-novelty rates.

Acceptance fixtures include a normal issue, no-publication interval, duplicate preprint and version of record, corrected article, retraction, inaccessible licensed content, malformed feed, poisoned document, apparently novel renamed method, relevant technique, and irrelevant high-prestige article. A passing end-to-end test proves that a permitted publication becomes a provenance-complete proposal and governed disposition. It must also prove that no source content can grant authority and no proposed technique can mutate research, trading, capital, or production state directly.

The first production cadence can be weekly while coverage and triage quality are calibrated; daily polling is enabled per source only when freshness value, licensing, cost, and operational capacity justify it.

> **Builder rule B10-BD08 — Build provenance before intelligence theater**  
> The first knowledge system succeeds by preserving and retrieving evidence reliably, not by presenting an impressive autonomous interface.

## Source note

Book III owns Research Intelligence semantics, including scheduled literature surveillance. Book IX owns the bounded knowledge-agent behavior; Books IV–VIII own evaluation and application of routed techniques.
