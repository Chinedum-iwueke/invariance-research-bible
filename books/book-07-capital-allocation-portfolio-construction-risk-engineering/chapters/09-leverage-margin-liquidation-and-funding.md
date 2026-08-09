<a id="b7-c09"></a>
# Chapter 9 — Leverage, Margin, Liquidation, and Funding

Leverage amplifies forecast, cost, gap, dependency, and operational error. Margin and liquidation rules turn market paths into nonlinear account states.

## 9.1 Leverage definitions

Track gross, net, delta-adjusted, risk, and balance-sheet leverage with explicit numerator and denominator. Net leverage can be small while gross liquidation risk is large. Derivatives require contract and collateral semantics.

## 9.2 Margin

Initial, maintenance, variation, portfolio, and venue margin differ. Margin depends on positions, marks, collateral, currency, offsets, and rules that can change. Simulators use versioned rule packs; live systems reconcile authoritative venue state.

## 9.3 Liquidation

Liquidation price is not one static formula across instruments and venues. Partial liquidation, fees, insurance mechanisms, mark price, cross versus isolated margin, and concurrent positions matter. Risk planning uses conservative distance-to-liquidation and stress paths, not UI estimates alone.

## 9.4 Funding and carry

Borrow, financing, perpetual funding, roll, and currency carry affect expected net return and can spike under stress. Funding forecasts carry uncertainty; accrued and projected amounts remain separate.

## 9.5 Controls

Reserve free margin, cap gross notional, stress collateral and FX, restrict concentration by venue, and define pre-liquidation deleveraging. Pending orders reserve capacity. Stale balances or reconciliation mismatches freeze risk-increasing actions.

> **Risk rule B7-RK09 — Margin is a state machine**  
> Leverage decisions use versioned instrument and venue rules, current reconciled collateral, pending exposure, and stress paths—not a single leverage multiplier.

## Source note

Book V supplies deterministic margin simulation surfaces; Book VIII owns venue mechanics and Book X live reconciliation.
