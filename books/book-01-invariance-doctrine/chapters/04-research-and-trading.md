<a id="b1-c04"></a>
# Chapter 4 — Research and Trading

Research and trading cooperate, but they do not perform the same institutional function. Research asks what can be known, under which assumptions, with what uncertainty, and through which evidence. Trading commits capital through decisions constrained by portfolio, risk, execution, and operations. Confusing the two allows commercial urgency to alter scientific claims or permits an elegant analysis to bypass the authority required for action.

The distinction is not a hierarchy in which researchers are pure and traders merely commercial. Trading produces observations that research cannot obtain from historical study alone. Researchers, in turn, create the evidence and limitations without which trading becomes unstructured risk-taking. The doctrine establishes reciprocal dependence with separate objectives and records.

## 4.1 Different questions

A research question can remain valuable even when it produces no strategy. It may determine that a representation leaks, that an effect is redundant, that a cost model is wrong, or that current data cannot distinguish between explanations. Its success criterion is the reliability and future usefulness of the knowledge produced.

A trading decision faces another question: given approved evidence, current state, portfolio exposure, costs, operational readiness, and authority, what action—if any—is permitted? The decision may rationally decline a scientifically supported opportunity because capacity is exhausted, risk is concentrated, execution is unreliable, or an external account constraint binds. Conversely, a portfolio may profit from beta, luck, or exposure without creating new research knowledge.

These questions generate different artifacts. Research produces question records, hypotheses, experiment specifications, runs, reviews, evidence dossiers, interpretations, and belief updates. Trading produces forecasts, portfolio intents, risk verdicts, orders, acknowledgements, fills, positions, reconciliations, incidents, and realized outcomes. A complete lineage connects them without pretending they are interchangeable.

## 4.2 Different clocks

Research can operate over months of conceptual development, days of experimentation, or minutes of anomaly triage. Trading operates under market and operational deadlines. The fastest clock must not acquire authority over the slower one merely through urgency.

An intraday anomaly may justify containment or reduced exposure before its cause is understood. It does not justify rewriting a model’s scientific record. A quarterly research review may retire a mechanism even if recent P&L is favorable. An incident may require an immediate deterministic halt followed by a slower diagnosis. The institution therefore separates observation, evaluation, and controlled change.

Book II defines the operating cadence and exception process. Constitutionally, the rule is that urgency changes the permitted response, not the truth status of a claim. Evidence gathered under emergency conditions retains the conditions under which it was gathered.

## 4.3 Discovery, monetization, and realization

The migration audit distinguishes three objects that the Founder’s Edition sometimes called alpha.

A **predictive edge** is evidence that causally available information changes the conditional distribution of a relevant future outcome. It may be too small, unstable, expensive, or capacity-limited to trade.

**Realizable alpha** is a conditional informational advantage for which prospective evidence supports positive economic value after applicable costs, execution constraints, capacity, uncertainty, and competition. It remains an estimate rather than a realized outcome.

**Realized active return** is an observed outcome relative to a specified benchmark and accounting convention. It is affected by exposure, sizing, leverage, execution, cost, and chance. It is neither necessary nor sufficient evidence of predictive edge by itself.

Research establishes and challenges the first two. Trading helps reveal whether the second survives operation and produces the third. The relationship is not one-way validation. A profitable outcome can coexist with a false mechanism; an unprofitable sample can coexist with a correctly estimated but uncertain edge. Attribution is required.

## 4.4 Separation of authority

The proposer of a claim may have insight unavailable to a reviewer, but also attachment and informational advantage that can distort evaluation. The laboratory may execute the design faithfully, but cannot decide that its own outputs deserve capital. A risk service may veto an order without possessing authority to create a larger allocation. Production may halt a system for safety without changing the registered scientific conclusion.

The institution separates:

- exploration, which proposes questions, representations, mechanisms, and hypotheses;
- experimental execution, which produces deterministic artifacts;
- independent evaluation, which tests methods, assumptions, leakage, robustness, and interpretation;
- governance, which controls permissions, protected data, exceptions, and maturity transitions;
- portfolio and production authority, which accepts capital and operational risk.

These functions can be performed by a small number of people or systems in an early institution, but conflicting permissions cannot be exercised by the same actor on the same decision without a documented exception and compensating review. Organizational size does not cancel separation of duties.

## 4.5 Promotion is not a score

A high Sharpe ratio, low p-value, accurate classifier, or persuasive dossier cannot promote a candidate. Promotion is a governed state transition based on a specified body of evidence and allowed authority. The evidence differs by stage.

Historical backtesting addresses behavior under recorded data and explicit assumptions. Robustness work attacks dependence on specification and selection. Shadow gathers prospective scientific evidence without orders. Execution replay tests production-equivalent internal logic without external submission. Demo exercises a simulated venue interface and order lifecycle. Micro-live exposes real liquidity and operational behavior with tiny capital. Production requires portfolio eligibility, a risk budget, and continued monitoring.

These environments are not rungs that automatically confer truth. A demo can be operationally correct while the hypothesis is weak. A shadow candidate can be scientifically promising while its execution path is unusable. [ADR-0004](../../../architecture/adrs/0004-orthogonal-state-models.md) therefore separates epistemic state, candidate maturity, validation environment, and operational state.

## 4.6 The value of not trading

An institution that equates research success with deployment will pressure every program toward a tradable conclusion. This creates strategies from weak evidence, hides null results, and discourages foundational questions whose benefit is indirect.

Not trading can be the correct output. The data may be insufficient, the edge may not survive cost, the mechanism may remain too uncertain for the proposed use, the portfolio may already contain the exposure, or the operational system may fail acceptance. A rejection or deferral preserves capital and directs attention toward the actual uncertainty.

The discipline also applies after deployment. Retirement is not an admission that earlier research was worthless. The environment may have changed; cost may have risen; capacity may have fallen; a stronger alternative may have displaced the candidate. A controlled retirement with preserved evidence is a successful institutional decision.

## 4.7 What performance can teach

Financial performance matters, but its interpretation is conditional. Realized returns can expose incorrect cost assumptions, hidden beta, tail dependence, sizing errors, execution divergence, or operational failure. They can also be too noisy to support a confident diagnosis over a short interval.

The institution therefore analyzes expected versus observed components: signal behavior, market exposure, cost, fill, latency, funding, risk actions, portfolio interaction, and unexplained residual. It considers sample size, state coverage, and predeclared expectations. Performance becomes a structured observation rather than a verdict.

This protects both science and capital. Research does not defend a model against contrary operational evidence, and production does not abandon a model because of one emotionally salient outcome. Each change follows evidence appropriate to the decision.

## 4.8 Reciprocal obligations

Research owes trading explicit scope, uncertainty, reproducible evidence, known failure modes, and honest economic assumptions. It must not hand production a promising narrative without a decision contract.

Trading owes research complete operational records. It must preserve skipped decisions, vetoes, orders, fills, reconciliations, incidents, and deviations rather than return only P&L. It must not modify scientific logic invisibly in production.

Governance owes both sides clarity about authority and exceptions. Research Intelligence owes the institution durable lineage and retrieval. Engineering owes deterministic services, tests, observability, and parity. No organization completes its work until the relevant evidence and lessons return to institutional memory.

Research and trading are thus neither rivals nor synonyms. Research develops and challenges justified beliefs. Trading acts within those beliefs and exposes them to additional reality. The institution remains scientific only while it preserves the distinction and the feedback between them.

## Source note

This chapter revises the Founder’s Edition, Chapter 4 (pp. 34–45), and integrates the later environment and authority architecture. Definitions of predictive edge, realizable alpha, and realized active return are controlled in the [series glossary](../../../glossary/GLOSSARY.md). Book II owns decision rights and promotion; Books VII–VIII own portfolio and execution science.

