<a id="b3-c17"></a>
# Chapter 17 — Corpus Governance and Adversarial Defense

Institutional memory contains untrusted external content, protected evidence, operational secrets, dissent, personal data, and model-generated proposals. Retrieval does not convert any of these into instructions. Corpus governance preserves evidence while preventing content, metadata, or derived indexes from bypassing authority.

## 17.1 Content and instruction channels

Source content is treated as data even when it contains commands, tool syntax, policy language, or prompts. System and task instructions arrive through authenticated control channels. Cognitive services cannot grant source text authority because it resembles an instruction.

Sanitization creates a derived view for safe processing. The raw captured artifact remains protected evidence and is not destructively “cleaned.” Detected injection or active content becomes a security finding linked to the source and recovery version.

> **Knowledge rule B3-KR17 — Evidence cannot issue authority**  
> Corpus content, retrieved text, metadata, embeddings, and model outputs may inform reasoning but cannot change policy, permissions, tool scope, or decision rights.

## 17.2 Threats to the corpus

Threats include source substitution, poisoned documents, prompt injection, malicious metadata, citation spoofing, duplicate flooding, embedding attacks, protected-data inference, corrupted lineage, and compromised contributor identity. Ordinary error—bad OCR, mistaken extraction, stale policy, or incorrect citation—can produce similar harm and receives integrity controls even without an attacker.

Source reputation informs review priority but never suppresses legitimate minority evidence automatically. Authentication proves origin, not truth.

## 17.3 Permissions and isolation

Access is scoped by identity, task, purpose, resource, action, environment, and time. Restrictions propagate through extracted text, summaries, embeddings, caches, graphs, counts, and exports. A frozen reviewer package prevents originator mutation while supporting governed requests for additional context.

Sealed holdouts are data-access classes, not validation environments. Query results, errors, timing, cache behavior, filenames, and aggregates are designed to avoid leaking protected partitions. Every exposure capable of influencing adaptation enters search history.

## 17.4 Privacy, rights, and retention

Corpus objects record classification, license, purpose limitation, consent or legal basis where applicable, region, retention, legal hold, and deletion requirements. Model training or fine-tuning requires its own authority; ordinary retrieval permission does not imply it.

Minimization applies to ingestion, context assembly, audit, and exports. Deletion propagates to derived indexes and backups under policy, with a permitted tombstone or certificate preserving the event.

## 17.5 Curatorial governance

Contributors can propose sources and corrections. The Librarian governs recovery and catalog quality. The Canon Curator governs canonical status. Security and rights authorities can quarantine or restrict content. These roles remain separated and their actions attributable.

Corpus disputes preserve competing interpretations and evidence. Quarantine limits use while investigation proceeds; it does not erase the object or declare its claims false.

## 17.6 Red-team and incident response

Authorized red-team tests cover injection, poisoning, privilege escalation, approval spoofing, exfiltration, sealed-data leakage, stale credentials, replay, and evidence corruption. Traps and canaries have scope, containment, cleanup, and contamination controls.

Findings become regression cases with severity, owner, remediation, verification, and knowledge return. Incident response follows Book II: contain, preserve evidence, diagnose, recover or retire, and learn.

## Source note

This chapter consolidates the Founder’s Edition, Chapters 50–54 (pp. 169–183), distinguishing protected data classes from validation environments and preserving untrusted source content without granting it instructional authority.
