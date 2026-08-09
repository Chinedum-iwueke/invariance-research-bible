<a id="b8-c05"></a>
# Chapter 5 — Funding, Basis, Liquidations, and Open Interest

Derivative state links price, leverage, collateral, and positioning. Common fields are venue constructions whose definitions and publication clocks must be preserved.

## 5.1 Funding and basis

Funding transfers and formulas vary by venue and contract. Record predicted and realized rates, interval, caps, reference inputs, source time, payment eligibility, and currency. Basis compares compatible instruments under explicit carry and maturity conventions.

## 5.2 Liquidations

Reported liquidation feeds may represent triggered orders, executed quantity, aggregated messages, or partial observations. They do not reveal all forced risk reduction. Venue liquidation logic depends on mark, margin tiers, fees, insurance, and account state.

## 5.3 Open interest

Open interest definitions, update frequencies, units, and historical revisions differ. Rising open interest does not identify long or short conviction by itself because contracts create paired positions.

## 5.4 Scientific use

Funding, basis, liquidation, and open-interest features carry event and availability times. Hypotheses state whether they proxy leverage, demand, crowding, carry, or stress and preserve alternatives. Their predictive use requires prospective evaluation after costs.

> **Execution rule B8-EX05 — Derivative telemetry keeps venue semantics**  
> No funding, basis, liquidation, or open-interest field is used without its contract, units, update process, availability, and coverage limitations.

## Source note

This chapter states data-contract requirements rather than universal empirical relationships.
