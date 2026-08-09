<a id="b9-c16"></a>
# Chapter 16 — Evidence-Governed Self-Improvement

Agent systems can propose changes to prompts, tools, retrieval, workflows, evaluations, and models. They cannot authorize their own production replacement.

## 16.1 Improvement object

Record observed failure or opportunity, proposed change, mechanism, affected contracts, training or tuning data, benchmark exposure, expected benefit, risks, evaluation plan, rollback, and owner.

## 16.2 Search and contamination

Repeated benchmark tuning overfits. Preserve all trials, maintain protected suites, rotate or generate fresh cases, and use prospective tasks. Agent-generated tests receive independent validation.

## 16.3 Promotion

Run offline regression, adversarial evaluation, shadow, canary, and monitored rollout. Independent reviewers decide. Improvements can be task-specific; aggregate gain cannot compensate for a severe new safety failure.

## 16.4 Learning from incidents

Incidents update threat models, tools, policies, tests, and training data with provenance. Secrets and harmful payloads are sanitized. The old version and evidence remain recoverable.

> **Agent rule B9-AG16 — Self-improvement is ordinary governed change**  
> Agents may diagnose and propose; independent evidence, authority, staged deployment, and rollback determine whether a new system version is adopted.

## Source note

This chapter applies Books II, IV, and VI promotion and search controls to agent systems.
