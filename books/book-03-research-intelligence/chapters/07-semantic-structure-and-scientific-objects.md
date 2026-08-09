<a id="b3-c07"></a>
# Chapter 7 — Semantic Structure and Scientific Objects

Retrieval units should follow scientific meaning rather than arbitrary token windows. Research Intelligence represents works, chapters, sections, definitions, propositions, proofs, equations, tables, figures, examples, footnotes, and references as linked objects whose source coordinates and surrounding argument remain recoverable.

## 7.1 Semantic retrieval units

A semantic retrieval unit is the smallest source-grounded object useful for a retrieval purpose while retaining the structure needed to interpret it. A definition can be retrieved alone for exact lookup, then expanded to its assumptions and examples. A result paragraph can be retrieved with the table and method section on which it depends.

Units record parent, sibling, continuation, prerequisite, caveat, citation, caption, and asset relationships. Boundaries follow recovered structure and may be corrected through versioned review.

Token windows can be derived for model context, but they are delivery artifacts rather than canonical scientific objects.

## 7.2 Equations and symbol scope

An equation object preserves source image or visual rendering, normalized mathematical representation where confidence permits, source coordinates, equation number, surrounding prose, symbol definitions, local scope, assumptions, dimensional information, and validation state.

Optical or language-model transcription is never accepted solely because it parses. Checks can compare visual structure, symbol counts, references, dimensions, and recomputation. Dimensional consistency cannot prove the equation or transcription correct.

> **Knowledge rule B3-KR07 — Non-prose evidence is first-class**  
> Equations, tables, figures, captions, notes, and bibliographies retain identity, coordinates, semantics, and quality independent of nearby prose; summaries cannot replace them as primary source objects.

## 7.3 Tables

A table object preserves title, caption, headers, units, row and column hierarchy, footnotes, panels, missing-value conventions, source coordinates, and adjacent interpretation. Structured cell extraction links to the visual source and records confidence.

Merged cells, spanning headers, and alignment can determine meaning. Flattened CSV output is derived and may be unsafe without structural review.

## 7.4 Figures

A figure object preserves image, caption, panels, axes, scales, units, legends, annotations, and textual references. A graph digitization is a separate derived dataset with method and uncertainty.

Visual resemblance or a model description is not evidence for numerical values that the figure does not report.

## 7.5 Citations and bibliographies

In-text citations link source spans to resolved bibliography entries where possible. A bibliography record establishes that the citing work referenced another work; it does not prove support for the local sentence. Citation validation in Chapter 11 evaluates that relationship.

Unresolved references remain explicit. Duplicate works and editions are reconciled without erasing the citation string printed in the source.

## 7.6 Deep reading

Deep-reading mode retrieves larger coherent structure when a question depends on definitions, method, result, and limitations. It can assemble a section tree, cited objects, neighboring equations, tables, or figures, and later qualifications.

Expansion is recorded in the retrieval manifest. A system should not present an isolated passage with the confidence of full-source review when only a fragment was inspected.

## Source note

This chapter consolidates the Founder’s Edition, Chapters 11–13 (pp. 43–51). It replaces canonical “chunking” with semantic retrieval units while allowing implementation-specific context windows as derived views.
