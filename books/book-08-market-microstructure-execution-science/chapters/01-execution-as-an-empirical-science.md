<a id="b8-c01"></a>
# Chapter 1 — Execution as an Empirical Science

Execution converts portfolio intent into venue events. Its quality depends on market state, venue rules, order lifecycle, latency, selection, and the institution’s own actions. It is measured prospectively and reconciled event by event.

## 1.1 Execution object

Record parent intent, decision benchmark, instrument and venue, side and quantity, urgency, risk constraints, child orders, acknowledgements, fills, cancellations, rejects, positions, costs, and terminal disposition. A fill price without the orders and opportunity set cannot establish execution quality.

## 1.2 Conditional evidence

Observed fills are conditional on historical routing. Unfilled and cancelled orders carry information about opportunity and selection. Transaction-cost analysis compares like intents under declared benchmarks while recognizing that counterfactual prices are unobserved.

## 1.3 Three evidence environments

Simulation estimates behavior under a model. Demo tests a venue-provided non-production environment with uncertain production equivalence. Live observation measures real interaction but is confounded by changing state and policy. Each environment answers different questions.

## 1.4 Research loop

Register an execution hypothesis; collect point-in-time events; estimate fill, cost, and adverse-selection distributions; replay; shadow; run bounded prospective tests; reconcile; publish limitations; and update only through governed policy.

> **Execution rule B8-EX01 — Every fill is selected evidence**  
> Execution analysis preserves the parent intent, available alternatives, order lifecycle, market state, and routing policy that made the fill observable.

## Source note

This chapter establishes execution science at the interface of Books V and VII. It makes no claim that simulated, demo, and live fills are equivalent.
