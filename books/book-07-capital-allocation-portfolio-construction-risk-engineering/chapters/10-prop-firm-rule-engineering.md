<a id="b7-c10"></a>
# Chapter 10 — Prop-Firm Rule Engineering

External account programs impose path-dependent constraints such as daily loss, total loss, trailing drawdown, minimum days, targets, consistency, prohibited behavior, and payout conditions. These are versioned legal and operational rules, not alpha logic.

## 10.1 Rule contract

Record provider, program and account type, jurisdiction, effective date, authoritative source, timezone, equity or balance basis, reset convention, open-P&L treatment, fees, trailing behavior, objectives, restrictions, exceptions, and ambiguity. Terms are reverified before use.

## 10.2 State machine

Represent evaluation, funded, review, breach, payout, reset, and closure states with explicit transitions. Daily boundaries follow the provider’s clock. Trailing thresholds update under the documented rule and never from an informal dashboard approximation.

## 10.3 Risk objective

Optimize survival and expected utility under rules, not merely target speed. Estimated pass probability, breach probability, funded lifetime, and time to target are model outputs with uncertainty. They are not service guarantees.

## 10.4 Portfolio controls

Use tighter internal buffers than external limits; reserve for gaps, fees, latency, and open risk; control correlation and event exposure; and block actions when rule state is uncertain. Multiple accounts may share market risk and must not be treated as independent diversification.

## 10.5 Governance

Terms can change. A rule-version update invalidates stale simulations and may require immediate risk review. The institution preserves the exact terms used for every decision.

> **Risk rule B7-RK10 — External rules are dated constraints**  
> No prop-firm parameter enters portfolio logic without authoritative source, program scope, effective date, interpretation, and uncertainty buffer.

## Source note

This chapter formalizes limitations identified in the Book II migration audit. It intentionally cites no current provider terms; those must be verified at decision time.
