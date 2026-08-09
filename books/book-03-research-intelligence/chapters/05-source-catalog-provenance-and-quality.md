<a id="b3-c05"></a>
# Chapter 5 — Source Catalog, Provenance, and Quality

Research Intelligence cannot reason reliably about a source it cannot identify. Titles and filenames are insufficient when works have editions, corrections, translations, preprints, accepted manuscripts, supplementary files, and licensed copies. The source catalog establishes identity, provenance, rights, and recovery quality before retrieval or synthesis.

## 5.1 Work, edition, and artifact

A **work** identifies the intellectual publication or controlled institutional object. An **edition** identifies a materially distinct version, release, translation, or manifestation. An **artifact** identifies the captured file or object from which recovery proceeds.

One work can have several editions and each edition several artifacts. Duplicate bytes share a content digest; similar content does not become one edition automatically. The catalog preserves relationships such as version-of-record, correction-of, translation-of, supplement-to, and supersedes.

## 5.2 Source identity

A source record includes stable internal identity, title, creators, publisher or issuing authority, publication and effective dates, edition or version, persistent external identifiers, capture origin and time, media type, content digest, language, rights, access classification, and retention policy.

External identifiers can be wrong or reused. Their values are evidence, not the internal primary key. Identity reconciliation records match basis and uncertainty.

> **Knowledge rule B3-KR05 — Capture before interpretation**  
> Every source entering canonical recovery receives immutable artifact identity, provenance, rights metadata, and a content digest before derived text, objects, summaries, or claims are published.

## 5.3 Provenance chains

Provenance links every derived object to the artifact, recovery pipeline, tool versions, parameters, human corrections, and publication event that produced it. A quotation resolves through claim and text spans to edition, page or location, and captured artifact.

Manual correction is an attributable transformation, not a hidden edit. The original recovery remains available where policy permits, allowing later tools to compare or improve it.

## 5.4 Quality is multidimensional

Source and recovery quality are not one score. Research Intelligence records separate assessments for metadata, text, OCR, reading order, headings, equations, tables, figures, citations, coordinates, and completeness. A born-digital PDF can have excellent text and broken reading order. A scan can have usable prose and unreliable equations.

Quality includes method, benchmark or sampling basis, reviewer, time, and uncertainty. Thresholds depend on use. Search discovery can tolerate lower text confidence than exact quotation or equation reuse.

## 5.5 Authority and curation

The Librarian owns source recovery, catalog integrity, identity reconciliation, deduplication, indexing readiness, and quality remediation. The Canon Curator evaluates whether an edition or claim receives canonical institutional status for a defined purpose.

Neither role can upgrade evidence through metadata. A prestigious publisher does not make every claim applicable; a clean extraction does not validate the source’s reasoning. Canonical status records authority and adoption, not infallibility.

## 5.6 Corrections, retractions, and loss

Corrections and retractions link to affected editions and claims. Retrieval surfaces the status with the historical source. A corrected edition does not erase decisions made from the earlier one; downstream lineage supports impact review.

If an artifact becomes inaccessible, the catalog retains permitted identity, digest, provenance, rights, and loss reason. Derived content follows license and retention obligations rather than remaining available merely because an index once captured it.

## 5.7 Scheduled literature surveillance

Research Intelligence maintains governed watchlists of finance, economics, statistics, machine-learning, market-microstructure, execution, portfolio, risk, and trading journals and other approved technical publications. Each watchlist records source identity, scope, authority class, access and licensing terms, acquisition method, owner, daily or weekly cadence, freshness objective, and failure policy. Scheduled collection captures issue feeds, tables of contents, metadata, abstracts, corrections, retractions, and full text only where access rights permit.

Knowledge agents compare each arrival with existing concepts, claims, methods, datasets, experiments, and unresolved questions. They produce source-linked novelty assessments, contradiction alerts, technique briefs, and candidate implications for current research programs. They distinguish a genuinely new method from a renamed, extended, replicated, or disputed prior result, and they preserve negative findings and applicability limits.

Publication does not confer adoption. A promising technique becomes a typed proposal routed to Book IV for hypothesis and search design, Book V for controlled experimentation, Book VI for learned-model methods, Book VII for portfolio and risk consequences, or Book VIII for execution testing. Trial registration, independent review, governance, portfolio eligibility, and environment promotion remain mandatory where applicable. Research Intelligence may recommend attention; it cannot apply a technique directly to production, allocate capital, or change policy.

> **Knowledge rule B3-KR05A — Current awareness is governed evidence intake**  
> Scheduled journal surveillance preserves rights, provenance, coverage, novelty basis, and downstream disposition; recency or publication prestige never substitutes for institutional validation.

## Source note

This chapter consolidates the Founder’s Edition, Chapters 6 and 8 (pp. 27–35). It preserves the separation between recovery stewardship and canonical judgment established in Books I–II and adds scheduled, rights-aware surveillance of approved scientific and industry journals as a target Research Intelligence capability.
