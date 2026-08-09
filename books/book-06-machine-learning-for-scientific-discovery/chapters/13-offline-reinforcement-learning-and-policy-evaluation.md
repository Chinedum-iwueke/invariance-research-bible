<a id="b6-c13"></a>
# Chapter 13 — Offline Reinforcement Learning and Policy Evaluation

Offline reinforcement learning attempts to evaluate or improve sequential policies from fixed historical data. Its central difficulty is not merely prediction. A learned policy may choose actions poorly represented by the behavior data, and value errors can compound across time.

## 13.1 Sequential contract

Define state, action, transition, reward, horizon, discounting, termination, behavior policy, observation process, constraints, and deployment interface. In markets, state is partially observed; rewards depend on costs and impact; actions alter exposure and perhaps observations; the environment is non-stationary and multi-agent.

An OHLC backtest is not automatically an RL environment. Its fill and impact model must support the actions a policy can propose.

## 13.2 Coverage and shift

Offline data identify policy behavior only where state-action coverage and modeling assumptions suffice. Extrapolated values for unsupported actions can be optimistic. Pessimism, behavior constraints, importance weighting, and model-based uncertainty address parts of the problem while adding assumptions.

[Wang et al. 2021](../../../bibliography/references.md#wang-et-al-2021-offline-rl) demonstrates substantial instability under distribution shift even with pretrained representations and concludes that offline RL can require stronger conditions than supervised learning. This evidence supports a conservative institutional boundary, not a universal impossibility theorem.

## 13.3 Off-policy evaluation

Evaluation methods include direct outcome models, importance weighting, doubly robust estimators, fitted value methods, and simulation. Each relies on behavior propensity, overlap, model correctness, or environment assumptions. Report effective sample size, weight concentration, support violations, horizon sensitivity, and disagreement among estimators.

Historical trading logs often omit rejected actions and exact behavior propensities. Approximate logging weakens identification.

## 13.4 Safety and constraints

Policy proposals remain inside hard risk and action envelopes supplied by Books VII–VIII. Constraint satisfaction in a learned simulator does not prove live safety. New policies begin in replay and shadow, with conservative fallback and independent authorization.

## 13.5 Research use

Offline RL may be useful for bounded execution or sequential selection problems with rich logged behavior, narrow action spaces, credible simulators, and strong overlap. When these conditions fail, contextual prediction plus explicit optimization is often easier to audit.

> **ML rule B6-ML13 — Unsupported actions have no earned value**  
> A policy cannot claim improvement from regions where behavior coverage, causal assumptions, or validated simulation do not support its value estimate.

## Source note

Technical cautions link to [Wang et al. 2021](../../../bibliography/references.md#wang-et-al-2021-offline-rl). Policy authority remains in Books VII–VIII and deployment in Book X.
