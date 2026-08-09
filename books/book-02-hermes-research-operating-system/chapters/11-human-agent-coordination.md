<a id="b2-c11"></a>
# Chapter 11 — Human–Agent Coordination

Agents extend institutional capacity by retrieving, synthesizing, proposing, executing bounded tools, and criticizing work. They do not erase accountability. Hermes coordinates humans and agents through the same typed artifacts and explicit authority model while recognizing different failure modes.

## 11.1 Capability profiles and task instances

An agent profile describes a reusable capability: intended role, model and tool requirements, context policy, prohibited actions, output contract, evaluation, and escalation behavior. A task instance binds that profile to a specific charter, identity, evidence set, budget, and deadline.

Profiles are not offices. Naming an agent “Governor,” “Validator,” or “Senior Researcher” does not grant institutional authority. The task instance receives only the permissions required for its work.

## 11.2 Decision packets

When human judgment is required, the agent produces a decision packet containing the decision requested, applicable authority, evidence and primary links, alternatives, dissent, uncertainty, conflicts, conditions, expiry, and consequences of action or delay.

The surface must support review rather than steer approval through selective presentation. Material omissions, unavailable evidence, and model uncertainty are visible. The human can approve, reject, defer, request additional evidence, narrow scope, or escalate.

> **Operating rule B2-OR11 — Human approval is substantive**  
> A required human decision cannot be replaced by acknowledgement, inactivity, default acceptance, or an interface that withholds the evidence needed for accountable judgment.

## 11.3 Context and provenance

Agent outputs identify the profile and task, model runtime and version where available, governing instructions, retrieved sources, tool actions, input artifact versions, and output identity at a level proportionate to consequence. Secret, private, and irrelevant content is minimized rather than copied into general traces.

Research Intelligence—not the model context—holds durable memory. A later model should be able to recover the decision through institutional artifacts without reconstructing hidden chain-of-thought. Required rationale consists of claims, evidence, alternatives, calculations, critiques, and decisions.

## 11.4 Escalation and refusal

An agent stops or escalates when authority, information, tool permission, budget, or safety conditions are insufficient. It reports the exact blocker and the least additional authority or evidence required. It does not improvise credentials, broaden data access, or reinterpret policy.

Refusal is itself a terminal task disposition. Repeated failure does not justify bypassing a control. A different worker inherits the same charter unless governance amends it.

## 11.5 Independence and correlated failure

Multiple agents can create useful specialization and criticism, but shared model families, prompts, sources, tools, or evaluators create correlated failure. Independent validation records these dependencies and uses deterministic checks, alternative models, human expertise, or separated evidence where appropriate.

Agreement among agents is not consensus evidence. Disagreement is preserved and resolved by the accountable process, not hidden through majority vote.

## 11.6 Evaluation and change

Agent evaluation covers factual grounding, citation fidelity, tool behavior, scope adherence, calibration, security, reproducibility, escalation, and downstream decision quality. A model upgrade is a system change requiring contextual regression tests before it replaces a production profile.

Book IX owns agent construction, communication, context, and evaluation methods. Book II owns the operating interface: what role is requested, what authority it lacks, what artifact it must return, and who decides what follows.

## Source note

This chapter consolidates the Founder’s Edition, Chapters 15–19 and 32–33 (pp. 56–70 and 111–116). Detailed agent architecture is relocated to Book IX; decision rights remain here.
