<a id="b8-c14"></a>
# Chapter 14 — Cost Models and Backtest Parity

Historical simulation uses execution models calibrated from observed evidence. Parity means assumptions and discrepancies are measurable, not that simulated fills equal live fills.

## 14.1 Model layers

Model spread and quote availability, latency movement, fill probability, queue, partial fill, fees, funding, impact, order rejection, and terminal handling separately. Complexity follows data support.

## 14.2 Calibration

Fit on point-in-time execution episodes with policy and venue versions. Preserve cancelled and unfilled intents. Evaluate conditional distributions, tails, support, and drift on protected prospective data.

## 14.3 Parity metrics

Compare decision-to-order mapping, fill rate, delay, price deviation, cost components, adverse selection, position path, rejects, and reconciliation. Differences feed model updates under new versions.

## 14.4 Conservative use

When evidence is weak, simulate scenarios or bounds. A zero-cost or immediate-fill assumption is a diagnostic baseline, not deployability evidence.

> **Execution rule B8-EX14 — Parity is a discrepancy ledger**  
> Simulation quality is judged by versioned comparisons with prospective execution and explicit residual error, not by declaring a model realistic.

## Source note

Book V implements simulation contracts; this chapter supplies empirical calibration and parity requirements.
