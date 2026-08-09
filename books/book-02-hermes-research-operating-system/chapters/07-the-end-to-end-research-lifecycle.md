<a id="b2-c07"></a>
# Chapter 7 — The End-to-End Research Lifecycle

The research lifecycle is not a conveyor belt from idea to production. It is a governed network in which questions can close, experiments can invalidate themselves, candidates can remain scientifically useful without becoming tradable, and production evidence can return a claim to investigation.

## 7.1 Lifecycle objects

The lifecycle moves through linked objects rather than one overloaded status:

1. anomaly or knowledge gap;
2. scoped research question;
3. registered hypothesis and alternatives;
4. representation and dataset contracts;
5. experiment specification and trial family;
6. immutable runs and evidence artifacts;
7. independent evaluation and evidence dossier;
8. maturity decision;
9. authorized environment execution;
10. portfolio and production decisions;
11. monitoring, demotion, retirement, and learning.

Each object has its own identity and state. A new experiment version does not overwrite its hypothesis; a candidate decision does not change the epistemic record automatically.

## 7.2 Orthogonal state

Hermes maintains epistemic state, candidate maturity, validation environment, and operational state separately. Epistemic state belongs to evidence semantics. Candidate maturity belongs to governance. Validation environment states where evidence was produced. Operational state describes whether a deployed capability is ready, running, degraded, or halted.

> **Operating rule B2-OR07 — No state inheritance**  
> Entry into an environment, successful operation, or favorable outcome does not automatically confer epistemic support, candidate maturity, portfolio eligibility, or production authority.

A governed transition may cite evidence from several environments and update maturity. It cannot collapse the four axes for convenience.

## 7.3 Discovery and candidate formation

Research begins with a question, not a strategy wrapper. Signal evidence, forecasting value, risk control, and execution improvement are typed contributions. Monetization design follows evidence about the underlying relationship but remains another registered search.

Not every hypothesis creates a candidate. A valid negative result can close the question. A useful market model can inform risk without generating a signal. Candidate formation states the decision rule, expected contribution, costs, constraints, and intended portfolio role.

## 7.4 Evidence progression

Historical backtest and robustness evidence precede prospective environments when applicable, but the sequence is not a universal ladder. Shadow records frozen decisions against unfolding outcomes without orders. Execution replay passes events through production-equivalent logic without venue submission. Demo tests a simulated or paper venue’s API. Micro-live uses tiny real capital. Production operates an approved candidate under risk budget.

Each environment has entry authority, permitted actions, required artifacts, exit criteria, and failure response. Chapter 14 defines their contracts.

## 7.5 Feedback and return paths

Lifecycle movement is reversible. A representation defect can invalidate runs. New evidence can weaken a supported claim. An incident can quarantine an implementation while leaving the hypothesis unresolved. Cost deterioration can remove portfolio eligibility while prediction remains present.

Demotion preserves the reason, evidence, effective time, affected versions, and remediation requirements. Retirement closes authorized use but preserves history subject to retention policy.

## 7.6 Terminal disposition

Every branch ends in an explicit disposition: advanced, rejected, invalid, deferred, superseded, quarantined, retired, or unresolved with a review date. Abandoned work cannot remain an invisible branch that later search mistakes for unexplored territory.

The lifecycle’s product is not promotion. It is a defensible change in institutional knowledge and authority, including the decision that no action should follow.

## Source note

This chapter revises the Founder’s Edition, Chapters 7, 9–10, and 22 (pp. 30–41 and 78–80). It corrects the omitted replay and demo environments and applies ADR-0004’s orthogonal state model.
