<a id="b4-c11"></a>
# Chapter 11 — LLM-Guided Scientific Proposal

Language models can connect literature, institutional evidence, mechanisms, and research-language components to propose hypotheses at a scale that changes the search process. Their output is proposal, not discovery. The laboratory records model-assisted generation, grounding, ranking, and human selection as adaptive search.

## 11.1 Proposal inputs and outputs

An LLM proposal task receives a bounded question, evidence dossier, controlled vocabulary, eligible representations and tools, prior-work comparison, charter, and output contract. It returns a registration-ready candidate or an explicit failure, with claims, citations, mechanism or predictive rationale, alternatives, representation, expected observations, falsification, and uncertainty.

The context manifest records model and service version, instructions, retrieved objects, tool calls, generated alternatives, sampling configuration where available, and selected output. Hidden chain-of-thought is not required; durable scientific rationale is.

## 11.2 Grounding and novelty

Citations are replayed to primary evidence. A proposal distinguishes source-supported statements from synthesis and speculation. Novelty uses nearest-prior comparison across claim, mechanism, representation, data, method, and experiment—not a model’s assertion that an idea is novel.

Models can reproduce memorized or corpus-present ideas without recognizable wording. Training-cutoff claims are imperfect contamination evidence and do not establish absolute novelty.

> **Discovery rule B4-DR11 — Generation expands search, not authority**  
> Every generated and viewed proposal enters search history; model ranking, fluency, agreement, or self-critique cannot grant evidential, governance, or promotion status.

## 11.3 Evidence from scientific-discovery studies

Recent research has evaluated LLM systems that retrieve inspirations, compose hypotheses, and rank them in bounded domains. MOOSE-Chem, for example, tested rediscovery of chemistry hypotheses using a curated post-cutoff benchmark and reported both useful retrieval behavior and limitations in hypothesis ranking ([Yang et al., 2025](../../../bibliography/references.md#yang-et-al-2025-moose-chem)).

This is domain- and benchmark-specific evidence. Rediscovering a held-out published hypothesis is not the same as generating a novel market hypothesis, validating it, or earning alpha. Book IV uses such work to motivate evaluation design, not capability claims about Hermes.

## 11.4 Generation strategies

Strategies include independent sampling, retrieval-conditioned synthesis, analogy, decomposition, critique and revision, debate, evolutionary mutation, and tool-grounded formalization. Each strategy creates different dependence and selection.

Self-evaluation can help filter obvious defects but shares model failure modes. Independent human, model, and deterministic checks are designed around correlated error rather than vote count.

## 11.5 Safety and scope

Proposal services cannot execute arbitrary code, acquire protected data, change their charter, or initiate capital-bearing action. Retrieved source instructions are treated as untrusted content. Sensitive market, personal, licensed, and operational information is minimized.

The service escalates when evidence is unavailable, definitions conflict, or a proposed experiment exceeds authority. Refusal and uncertainty remain valid outputs.

## 11.6 Evaluation

Evaluation separates grounding, internal coherence, plausibility, novelty relative to the corpus, discriminating predictions, testability, safety, cost, and later empirical performance. Judges are blinded where feasible and protected from model-authorship cues.

The selection funnel is evaluated, not only the best examples. A system that generates thousands of weak candidates and showcases one plausible result must expose the denominator and verification cost.

## Source note

This chapter defines the governed interface for LLM-assisted hypothesis proposal and cites recent primary research as limited external evidence. Agent construction and evaluation are owned by Book IX.
