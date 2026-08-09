# Cross-Reference Standard

**Status:** Controlled standard

## Identifiers

Books use Roman numerals in prose and zero-padded directory numbers in paths. Chapters use `B{book}-C{chapter}` as stable semantic identifiers, for example `B3-C11`. Figures, tables, definitions, principles, propositions, and appendices add a type and sequence: `B3-F04`, `B5-T07`, `B1-D12`, `B1-PR03`, `B6-P02`, and `B7-A03`.

Identifiers do not encode a heading title, page number, implementation version, or publication status. If chapters are reordered, an explicit migration table preserves old identifiers or records supersession; identifiers are never silently reused for a different object.

## Markdown anchors and links

Chapter files begin with an explicit HTML anchor followed by the title:

```markdown
<a id="bN-cNN"></a>
# Chapter NN — Descriptive Chapter Title
```

Cross-volume prose uses a descriptive relative link on first reference. After the target chapter exists, an example from another book would link “the evidence dossier contract” to `../../book-03-research-intelligence/chapters/11-evidence-dossiers.md#b3-c11`. Later nearby references may use “Book III, Chapter 11.” A bare identifier is reserved for tables, schemas, and indexes. Do not commit a link to a planned file before that file exists.

## Reference discipline

A cross-reference states the dependency rather than merely gesturing toward another volume. Non-owning books may summarize the minimum interface in one paragraph, then link to the authoritative treatment. If the local treatment changes the concept, it requires an ADR and an update to the ownership map.

References to Founder’s Editions use source book, chapter, and printed PDF page during migration. Once Version 2 is canonical, reading prose references Version 2 chapters; the migration ledger retains the source coordinates.
