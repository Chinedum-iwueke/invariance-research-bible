<a id="b9-c05"></a>
# Chapter 5 — Independent Evaluation and Governance Agents

Evaluation agents test claims, artifacts, contracts, and policy compliance. Governance agents assemble decision packets and enforce workflow; they do not become the accountable decision maker.

## 5.1 Independence

Independent evaluation requires separate task authority, protected prompts and evidence where needed, no hidden access to the generator’s rationale, and an accountable review path. A second call to the same model is corroboration, not independent governance.

## 5.2 Evaluation work

Validate schemas and lineage, reproduce calculations, seek counterexamples, test leakage and selection, compare alternatives, inspect limitations, and classify failures. Evaluators report unresolved uncertainty and dissent.

## 5.3 Governance work

Check completeness, state transitions, decision rights, conditions, expiry, conflicts, and audit trail. Governance agents can block incomplete automation under policy but cannot approve substantive exceptions without authority.

## 5.4 Anti-collusion

Prompts and communication are logged; evaluator identities rotate where appropriate; benchmark leakage is controlled; and agreement rates are not treated as correctness.

> **Agent rule B9-AG05 — Review independence is architectural**  
> Different labels or model instances do not create independent review without separate authority, evidence policy, incentives, and accountable disposition.

## Source note

This chapter implements Book II’s challenge and separation-of-duty controls.
