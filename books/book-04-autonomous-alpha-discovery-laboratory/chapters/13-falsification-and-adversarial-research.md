<a id="b4-c13"></a>
# Chapter 13 — Falsification and Adversarial Research

Adversarial research seeks observations and analyses that distinguish the focal claim from credible alternatives. It is not ritual hostility, a requirement that every hypothesis be rejected, or a red-team veto detached from evidence.

## 13.1 The adversarial plan

The hypothesis contract supplies predicted observations, boundary conditions, alternatives, invalidity risks, and failure criteria. An adversarial plan maps each to tests, required data, protected evidence, and interpretation.

Tests can challenge temporal availability, sample formation, representation, baseline, dependence, costs, capacity, mechanism, stability, and implementation. The strongest challenge targets the claim’s consequential weak point rather than accumulating generic robustness checks.

## 13.2 Red-team independence

The Red Team receives a frozen candidate package and explicit authority to inspect, reproduce, challenge, and request additional context. It cannot alter the reviewed version or promote its own alternative. Shared data, code, models, prompts, incentives, and organizational reporting are recorded as independence limitations.

> **Discovery rule B4-DR13 — Criticism must be discriminating**  
> An adversarial finding identifies the claim or artifact challenged, the competing explanation, the evidence produced, and the interpretation warranted; skepticism alone is not a scientific result.

## 13.3 Negative controls and placebos

Negative controls use variables, outcomes, populations, or times where the proposed process predicts no relationship. Placebo tests apply the design where an effect should not occur. Their validity depends on whether the control truly lacks the causal or predictive pathway under question.

A failed placebo can reveal leakage, confounding, shared exposure, or a broader mechanism. Passing many correlated placebos does not prove absence of every artifact.

## 13.4 Perturbation and stress

Perturbations vary definitions, timing, samples, costs, parameters, and environmental assumptions that could plausibly alter the result. Stress tests examine extreme but coherent conditions and joint failure. The plan explains why each perturbation bears on the mechanism or decision.

Broad robustness can be false when shared errors persist; narrow effects can be real when mechanisms create thresholds. The response surface and failure boundary are more informative than a pass count.

## 13.5 Reproduction and replication

Computational reproduction checks the same inputs and method. Independent reimplementation targets shared code defects. Replication uses new data aimed at the same question. Prospective observation fixes the claim before later outcomes.

Inconsistent results trigger diagnosis of scope, measurement, implementation, environment, and statistical uncertainty. They do not automatically declare one study fraudulent or irrelevant.

## 13.6 Decision outcomes

Adversarial review can admit evidence, qualify scope, request repair, invalidate runs, weaken or reject a claim, preserve dispute, or recommend a new experiment. Governance decides candidate maturity separately.

The originator responds through an attributable artifact. Endless rebuttal is prevented by budgets and stopping rules; unresolved disagreement remains visible.

## 13.7 Learning from successful attacks

Each confirmed defect becomes a regression case, retrieval target, language constraint, detector improvement, or policy proposal. The institution measures adversarial value by consequential errors found and prevented, not rejection rate.

## Source note

This chapter operationalizes Book I, Chapter 7 and Book II’s independent-review boundary. Book V owns deterministic adversarial experiments; Book IX owns construction and evaluation of red-team agents.
