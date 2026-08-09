<a id="b2-c09"></a>
# Chapter 9 — Experiment and Evidence States

An experiment, a run, a result, and a belief are different objects. When one status field attempts to describe all four, invalid execution can be mistaken for a scientific null, favorable output can be mistaken for supported belief, and operational completion can be mistaken for review.

Hermes therefore governs experiment execution and evidence disposition through linked but distinct records.

## 9.1 Specification and run

An experiment specification defines the executable test of a registered hypothesis. It references the question, hypothesis version, representation, dataset identities, temporal policy, universe, parameters or search space, metrics, exclusions, cost assumptions, environment fingerprint, and expected artifacts.

A run is one attempted execution of that specification. It has its own identity, start and end times, executor, input digests, code and environment identity, logs, resource use, output digests, and terminal status. Retry creates a new run linked to the failed attempt.

The specification can be valid while a run fails. A run can complete while the design is scientifically invalid. Hermes preserves both distinctions.

## 9.2 Run states

The controlled run states are:

- **queued** — accepted but not started;
- **running** — execution has begun;
- **completed** — declared outputs were produced;
- **interrupted** — execution stopped before completion;
- **failed** — an execution or infrastructure error prevented completion;
- **invalidated** — outputs exist but cannot support their intended interpretation;
- **cancelled** — withdrawn by authorized action before completion.

Completed means mechanically complete, not scientifically successful. Validation attaches a separate disposition and reason.

## 9.3 Evidence artifacts

Primary artifacts are emitted by the authoritative data, calculation, or laboratory service. Derived reports, figures, summaries, and model interpretations link back to them. An evidence bundle records specification and run identities, inputs, outputs, diagnostics, limitations, search history, and applicable access restrictions.

Artifact integrity uses content identity and signed or authenticated provenance where consequence warrants. Immutability protects a version; it does not prove correctness.

> **Operating rule B2-OR09 — Completion is not validity**  
> No completed run contributes scientific evidence until its identity, inputs, implementation, temporal integrity, declared diagnostics, and applicable review requirements have been evaluated.

## 9.4 Evidence disposition

An evaluator can classify a bundle as admissible, qualified, invalid, contaminated, superseded, or pending. The disposition states which claims the evidence can bear on and which limitations remain. A qualified bundle can support a narrow claim while failing a broader one.

Invalidity reasons are typed: data defect, leakage, specification violation, implementation defect, environment mismatch, incomplete artifacts, unauthorized access, or another explicit cause. Invalid work remains part of search and operational history but does not become negative scientific evidence.

## 9.5 Epistemic assessment

Research Intelligence preserves claim-level epistemic assessments such as proposed, disputed, supported, weakened, rejected, or retired. Hermes requests and records the assessment used by a decision; it does not infer belief state from metrics.

Evidence can bear differently on related claims. A result may support prediction while weakening a proposed mechanism. A cost study may leave prediction unchanged while eliminating realizable alpha. The evidence dossier keeps those claim relationships explicit.

## 9.6 Assurance

Assurance covers schema validation, reproducible input resolution, deterministic rerun where applicable, artifact completeness, timestamp and availability checks, unauthorized mutation, retry lineage, and invalidity propagation. Downstream decisions are discoverable when an evidence bundle is invalidated later.

The objective is not a decorative state machine. It is the ability to reconstruct what ran, whether it ran as specified, what evidence it produced, which claims could use that evidence, and which decisions depended on it.

## Source note

This chapter develops the Founder’s Edition, Chapters 10 and 22 (pp. 39–41 and 78–80). Bulletproof BT owns deterministic experiment execution; Book III owns claim and evidence semantics; Hermes owns admissibility workflow and decision use.
