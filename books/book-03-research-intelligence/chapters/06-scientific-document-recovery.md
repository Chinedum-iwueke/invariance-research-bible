<a id="b3-c06"></a>
# Chapter 6 — Scientific Document Recovery

Ingestion is not copying text into an index. Scientific documents encode argument through hierarchy, reading order, typography, equations, tables, figures, notes, references, and spatial relationships. Recovery reconstructs enough of that structure to support citation, deep reading, and scientific-object extraction without hiding uncertainty.

## 6.1 The recovery sequence

The controlled sequence is:

1. capture and catalog the immutable artifact;
2. classify media and select a recovery path;
3. render pages or equivalent visual units;
4. recover text, geometry, and reading order;
5. detect hierarchy and non-prose objects;
6. reconcile citations, references, captions, and continuations;
7. evaluate quality by object type;
8. review or remediate material defects;
9. publish versioned recovered structure;
10. build derived indexes and semantic objects.

Publication is reversible: a better pipeline creates a new recovery version linked to the same source artifact.

## 6.2 Born-digital, scanned, and mixed sources

Born-digital documents may expose text and layout objects directly, but embedded encodings, ligatures, columns, and drawing primitives can still corrupt recovery. Scanned documents require OCR and layout reconstruction. Mixed documents can contain searchable prose beside image-only equations or figures.

The pipeline classifies at page and object level rather than assuming one method fits the file. OCR confidence never substitutes for visual review of consequential passages.

## 6.3 Geometry and reading order

Recovered spans retain page, bounding region, reading-order position, and relationship to columns, footnotes, captions, and marginalia. The visual page or source coordinate remains available for citation replay.

Reading order is an inference. Multi-column layouts, sidebars, tables, and continuing footnotes can produce fluent but false prose when concatenated incorrectly. Quality checks sample transitions and structural boundaries, not only character accuracy.

> **Knowledge rule B3-KR06 — Structure survives recovery**  
> Scientific recovery preserves hierarchy, location, continuation, and non-prose relationships sufficient to reconstruct the source’s argument; plain extracted text is never treated as the complete source.

## 6.4 Headings and hierarchy

Hierarchy is inferred from bookmarks, typography, numbering, position, repeated headers, and content patterns. Each section links to its parent, siblings, source span, and recovery confidence. Running headers and tables of contents are not silently promoted into duplicate body sections.

Deep-reading retrieval can expand from a matched passage to its enclosing section, definitions, preceding assumptions, later caveats, and referenced objects.

## 6.5 Quality remediation

Material defects enter a remediation queue with source, object, defect type, severity, proposed correction, reviewer, and resulting recovery version. Human edits preserve the machine output and source image. Review priority follows downstream consequence and use frequency.

The institution does not require perfect recovery before any source becomes discoverable. It exposes quality and prevents low-confidence objects from supporting uses such as exact quotation, equation execution, or canonical definition without review.

## 6.6 Reproducibility and publication

Recovery records pipeline and dependency versions, configuration, language models or OCR engines, inputs, outputs, warnings, and resource use. Deterministic components should reproduce under the retained environment; probabilistic components retain seeds or variance evidence where feasible.

Published recovery is a derived edition view. It never replaces the captured source artifact or claim authority.

## Source note

This chapter revises the Founder’s Edition, Chapters 9–10 (pp. 37–42). Implementation topology and storage move to Book X; the recovery semantics remain authoritative here.
