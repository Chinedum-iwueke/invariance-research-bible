<a id="b9-c02"></a>
# Chapter 2 — Cognitive Services and Model Runtimes

Cognitive services provide generation, classification, extraction, retrieval planning, critique, summarization, code proposal, or tool-selection capabilities. Model runtimes are replaceable implementations behind those services.

## 2.1 Service contract

Define input schema, output schema, evidence policy, allowed tools, latency and cost envelope, determinism expectations, refusal and uncertainty semantics, data classification, evaluation suite, and fallback.

## 2.2 Runtime registry

Record provider, model and version, cutoff where known, context and output limits, deployment region, data handling, tool interface, safety profile, price, latency, and verified task performance. Mutable aliases do not identify a runtime release.

## 2.3 Routing

Route by task risk, data class, capability, cost, latency, and evaluation. High-impact tasks can require diverse models or deterministic validation. Model self-reported confidence does not determine routing authority.

## 2.4 Degradation

Runtime changes trigger regression evaluation. Fallbacks can narrow capability or require human review; they never inherit authorization merely because the primary runtime failed.

> **Agent rule B9-AG02 — Services own contracts; models supply behavior**  
> Model replacement is safe only when the cognitive service’s schema, permissions, evaluation, and limitations remain satisfied.

## Source note

This chapter extends Book III’s replaceable-runtime architecture and Book VI’s model governance.
