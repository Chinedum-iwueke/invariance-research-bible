<a id="b2-c14"></a>
# Chapter 14 — Shadow, Replay, Demo, Micro-live, and Production

Validation environments answer different questions. Hermes prevents evidence from being promoted by vocabulary and controls the permissions, entry conditions, artifacts, and exit decisions of each environment.

Historical backtest and robustness analysis precede these environments where applicable. They remain historical laboratory evidence.

## 14.1 Shadow

Shadow freezes decision logic and records hypothetical intents against unfolding markets without submitting an order. It tests prospective signal behavior, causal availability, decision cadence, and realized outcomes. It does not test venue integration or actual fills.

Required records include input availability, feature and model versions, signal, hypothetical intent, skips, expected outcome, realized outcome, and deviation from registered expectation.

## 14.2 Execution replay

Replay passes recorded or live-captured events through production-equivalent decision, risk, OMS, and adapter logic without venue submission. It tests ordering, state, rejection, sizing, reconciliation, latency assumptions, and deterministic reproducibility.

Replay fills are modeled evidence. They cannot establish actual queue position or market impact unless the model and claim support that interpretation.

## 14.3 Demo

Demo uses a venue’s simulated, paper, or test API and order lifecycle. It tests authentication, session behavior, order messages, acknowledgements, cancellations, rejections, and reconciliation. Demo liquidity and fill behavior may be artificial; demo success is engineering evidence, not prospective alpha evidence.

## 14.4 Micro-live

Micro-live uses deliberately tiny real capital under hard exposure, loss, leverage, permission, and time limits. It observes real venue behavior, liquidity, fees, funding, latency, fills, reconciliation, and operational response. Its purpose is information and safety validation, not income.

A small notional is not sufficient control. Correlated exposure, account reach, venue failure, credential scope, and automated loss limits remain bounded. Expansion never follows merely from a profitable sample.

## 14.5 Production

Production is capital-bearing operation by a production-eligible, portfolio-admitted candidate under an assigned risk budget, monitoring, reconciliation, and demotion or retirement controls. Every deployed version and configuration is identifiable.

> **Operating rule B2-OR14 — Environment evidence remains typed**  
> Evidence produced in one validation environment retains that environment’s limitations and cannot be represented as evidence from another.

## 14.6 Entry, exit, and rollback

Each environment defines entry authority, eligible package, data and venue access, risk ceiling, duration, evidence requirements, failure response, and closeout. Exit can advance, repeat, narrow, demote, quarantine, or retire. No environment guarantees progression.

Emergency controls can halt or reduce exposure. Restart requires resolution of the halt condition and fresh authorization where policy or package identity changed.

## Source note

This chapter revises the Founder’s Edition, Chapters 25–26 (pp. 88–93), adding the previously omitted execution replay and demo environments and correcting the earlier conflation of shadow with simulated orders.
