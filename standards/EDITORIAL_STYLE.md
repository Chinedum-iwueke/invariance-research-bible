# Series Editorial Style

**Status:** Controlled standard  
**Scope:** Books I–X and supporting canonical material

## Voice and argument

Write in a consistent institutional voice: precise, measured, technically literate, and explicit about uncertainty. Chapters develop an argument through sustained prose. Definitions, propositions, design rules, tables, equations, and diagrams support that argument; they do not replace it.

Avoid chat idiom, motivational filler, imagined dialogue, unsupported superlatives, rhetorical fragments, excessive one-sentence paragraphs, and repetitive contrast formulas. Do not imitate a living author. A chapter opening establishes its governing problem and dependency on prior volumes. A conclusion records what has been established, its limitations, and what the next chapter may assume.

## Claim discipline

Material claims use one of five labels when their status could be confused:

- **Doctrine:** a controlled institutional commitment.
- **Implementation fact:** behavior verified in a named code version, test, schema, or artifact.
- **Empirical result:** an observed result with data, method, uncertainty, and provenance.
- **Proposal:** a target design not yet implemented or adopted.
- **Inference:** a reasoned conclusion whose premises and uncertainty are stated.

An unlabeled sentence may explain or connect established material, but must never make planned capability sound implemented or institutional design sound empirically validated.

## Structure and ownership

Each major concept has one authoritative home in the [concept ownership map](../registers/CONCEPT_OWNERSHIP.md). Other books cross-reference that treatment and add only the local interface or consequence. Concise recapitulation is allowed when a reader cannot understand the local argument without it.

Use stable, descriptive Markdown headings. Link to files with repository-relative paths and to headings through explicit, durable slugs where ambiguity is possible. Mermaid is the canonical source format for maintainable architecture, state, and sequence diagrams. Every diagram receives an identifier, title, explanatory paragraph, and prose consistency check.

## Technical integrity

Equations define every symbol at first use. Examples state whether they are illustrative, synthetic, or empirical. Numerical claims include units, sampling basis, and applicable horizon. Negative results, rejected alternatives, uncertainty, failure modes, and boundary conditions are preserved. No architecture, model, or process is represented as a guarantee of profit.

## Editorial acceptance

A chapter is publication-ready only after terminology, continuity, ownership, claims, citations, diagrams, links, rhythm, and paragraph development have been checked. A book also requires a whole-volume continuity edit; the series requires a final cross-volume review.

