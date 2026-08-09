<a id="b1-c12"></a>
# Chapter 12 — Information, Causality, and Limits

Information, prediction, explanation, causality, and economic value answer different questions. Confusing them makes quantitative language sound stronger than the evidence. Invariance Research keeps them separate so that a formal measure, a forecasting gain, or a compelling mechanism cannot silently acquire conclusions it does not support.

## 12.1 Information is defined relative to variables

Shannon’s theory defines entropy and mutual information for specified random variables and probability models ([Shannon, 1948](../../../bibliography/references.md#shannon-1948)). The quantities are powerful and precise within that setting. They do not measure meaning, causal importance, executability, or profit by themselves.

For a discrete variable (X) with probability mass function (p(x)), entropy is

\[
H(X)=-\sum_x p(x)\log p(x).
\]

Mutual information is

\[
I(X;Y)=\sum_{x,y}p(x,y)\log\frac{p(x,y)}{p(x)p(y)},
\]

where (p(x,y)) is the joint mass function and logarithm base determines the unit. Estimation from finite, dependent market data introduces method-specific bias and uncertainty.

These definitions prevent metaphor from masquerading as calculation. “The market contains information” and “research reduces uncertainty” can be useful prose, but neither is a numerical claim until variables, distributions, estimators, and scope are specified.

## 12.2 Dependence is not economic value

Mutual information and other dependence measures can show that variables are statistically related under a distribution. They do not establish that information was available at decision time, that the relationship is stable, that it adds beyond existing inputs, or that an executable decision has positive net value.

Predictive edge requires causal availability and prospective relevance. Realizable alpha additionally requires costs, capacity, constraints, and implementation. A tiny dependence can be valuable at scale; a large dependence can be unusable because it concerns a target that cannot be traded or information that arrives too late.

> **Principle B1-PR11 — No inferential promotion by vocabulary**  
> A statistical dependence, information measure, prediction, explanation, causal claim, and realizable alpha remain distinct until evidence establishes each required bridge.

## 12.3 Prediction and explanation

A predictive model can work without identifying why. Such a model may be admissible for a bounded decision if prospective evidence, stability, monitoring, and failure controls are adequate. Its claim remains predictive.

An explanatory account identifies a mechanism and discriminating implications. It can improve transport, stress design, and diagnosis, but a plausible account is not validated by narrative coherence. Prediction can test implications of an explanation without exhausting it.

The institution values both and labels them. It does not reject useful prediction for lacking a complete theory, nor treat a theory as predictive evidence before its implications are observed.

## 12.4 Causal claims require identification

Causal questions concern interventions or counterfactuals: what would change if an action, rule, or condition changed? Statistical association alone does not identify that answer. Structural causal approaches make this distinction explicit by combining data with causal assumptions and an identification strategy ([Pearl, 2010](../../../bibliography/references.md#pearl-2010-causal-inference)).

Market causality is difficult, not impossible. Randomized interventions may be unavailable or unethical, but natural experiments, rule changes, instrumental variables, discontinuities, panel designs, structural models, and carefully bounded operational experiments can provide evidence under different assumptions. Every design exposes what remains unidentified.

Mechanism claims and causal estimates are also distinct. A mechanism can be plausible without an identified effect size; a causal effect can be identified under assumptions without a complete participant-level story.

## 12.5 The limits of observation

Market data reflect actions that occurred under existing rules and policies. They may not reveal latent intentions, unsubmitted orders, constrained alternatives, or responses to interventions never attempted. Selection, strategic adaptation, feedback, and measurement can make observational equivalence persistent.

The institution records these limits rather than filling them with confidence. Simulation can test consequences of a specified artificial world, not prove that the world matches the market. Synthetic data can exercise systems and hypotheses, not manufacture independent empirical evidence.

Some questions remain underidentified at the available resolution. A useful decision can still be made through robust bounds, scenario analysis, or conservative control, provided the unresolved claim is not misreported as solved.

## 12.6 Compression and representation

Every operational representation compresses. The question is which distinctions it preserves for the decision. Lossless compression is defined relative to exact reconstruction of an encoded object; scientific sufficiency is relative to a claim. A compressed representation can reconstruct a series while omitting venue state needed to explain execution.

Representation comparison may use information measures, predictive scores, invariance tests, and domain diagnostics. No single metric establishes sufficiency. The fit process, finite-sample estimator, search exposure, and downstream consequence remain part of the evidence.

## 12.7 Institutional limits

The institution has finite attention, data rights, computation, experimental access, and capital. Some information is too costly, prohibited, or dangerous to obtain. Some interventions impose unacceptable market, legal, or ethical costs. Scientific ambition operates inside these constraints.

The governing response is explicit scope. Invariance Research distinguishes what was observed, what was inferred, what was assumed, and what remains unknown. It seeks stronger bridges among information, prediction, explanation, causality, and action without pretending those bridges exist by definition.

## Source note

This chapter revises the Founder’s Edition, Chapters 8, 21, 22, 26, and 27 (pp. 75–87, 252–280, and 317–344). Formal estimation and causal discovery methods belong to Books IV and VI; economic realization belongs to Books VII–VIII.
