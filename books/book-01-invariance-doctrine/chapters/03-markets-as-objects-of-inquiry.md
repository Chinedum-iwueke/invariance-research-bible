<a id="b1-c03"></a>
# Chapter 3 — Markets as Objects of Inquiry

A price series is not a market. It is one record produced by a market under a particular sampling rule, clock, venue, instrument definition, and data-recovery process. A candle compresses many events into a small set of numbers. A trade reports an execution but not every intention that preceded it. A quote reports displayed willingness under venue rules but not hidden liquidity, inventory pressure, or the constraints governing participants. Even a detailed event stream is an observation of the system, not the system itself.

This distinction defines the scientific object of Invariance Research. The institution does not treat recorded prices as self-explanatory facts from which strategies can be mined without theory. It studies a partially observed, interactive environment whose measurements depend on representation and whose behavior may change when participants, incentives, information, technology, regulation, and capital change.

The claim is a research stance, not a declaration that every useful market model must be complex. Simple models can be powerful precisely because they isolate a mechanism or provide a hard benchmark. The doctrine concerns what the institution may infer from them. A model’s usefulness within a scope does not turn its simplifications into properties of the market.

## 3.1 Observation is constructed

The phrase *raw data* is convenient but easily misleading. Exchange messages, vendor files, trades, quotes, bars, funding records, open interest, liquidations, and reference data have already passed through definitions and systems. They embody event semantics, clocks, aggregation, correction policy, survivorship, venue scope, and availability delay. A researcher receives a constructed observation.

This does not imply that data are arbitrary. It implies that scientific claims must identify how observations were produced and when they became available. The same event may have an exchange event time, a local receive time, a corrected publication time, and an ingestion time. A historical universe may differ from the set of instruments visible today. A corrected record may describe the past more accurately while remaining unavailable to the decision that was made in the past.

Consequently, a market hypothesis includes its observational contract. It specifies instruments, venues, clocks, sampling, availability, universe formation, transformations, target horizon, and relevant costs. Without these, “the market” and “the signal” are underspecified.

> **Principle B1-PR03 — Observational explicitness**  
> A market claim is interpreted only within the data, time, instrument, venue, representation, and decision scope that produced its evidence.

## 3.2 Adaptive and interactive behavior

Economic systems contain participants who respond to prices, constraints, beliefs, and one another. Their actions contribute to the aggregate state to which they subsequently react. W. Brian Arthur’s account of complexity economics emphasizes this recursive formation of patterns, while Andrew Lo’s Adaptive Markets Hypothesis develops an evolutionary perspective on changing market behavior ([Arthur, 1999](../../../bibliography/references.md#arthur-1999-complexity); [Lo, 2004](../../../bibliography/references.md#lo-2004-adaptive-markets)). These are influential frameworks, not universal empirical laws, and Version 2 treats them as intellectual support for a cautious institutional stance.

The stance has several consequences. First, a regularity may be conditional on the population and constraints that sustain it. Second, publication or exploitation may alter the opportunity. Third, a stable-looking sample may combine several different mechanisms. Fourth, an intervention by the institution can change the execution environment it is attempting to measure.

Adaptation does not imply that every edge decays on a predictable schedule or that permanent regularities cannot exist. Nor does it prove that all regimes are continuous latent states rather than useful discrete approximations. It means that stability is an empirical property to be tested and monitored rather than granted by historical fit.

The information economics of markets provides another reason for care. Grossman and Stiglitz showed, within a formal model, the tension between costly information acquisition and perfectly revealing prices: if prices fully reflected costly information, the private incentive to acquire it would disappear ([Grossman and Stiglitz, 1980](../../../bibliography/references.md#grossman-stiglitz-1980)). The result does not prove that every observed pattern is exploitable. It demonstrates that information, incentives, and price formation cannot be separated casually.

## 3.3 Hidden state and imperfect proxies

Many objects of interest are not directly recorded. Liquidity stress, inventory pressure, participant urgency, information arrival, latent risk, and market regime are inferred through proxies and models. A proxy may be useful without uniquely identifying the phenomenon. Funding can reflect leverage and demand while also responding to venue mechanics. Spread can reflect risk, competition, tick size, fees, and latency. Volatility can describe dispersion without explaining its cause.

The institution therefore distinguishes observation, representation, latent-state estimate, mechanism claim, and decision. A model may estimate a regime from causally available variables. That estimate is not the regime itself. A graph may relate funding to subsequent reversals. The relation is not a causal explanation. A plausible participant story is not evidence merely because it sounds economic.

Mechanism work proceeds through competing explanations and discriminating observations. If liquidity exhaustion is proposed, the research design asks what else should be observed, where the effect should weaken, and what alternative artifacts could produce the same pattern. Some useful predictive claims will remain mechanism-uncertain. They can be evaluated and bounded as predictive claims without being promoted to causal knowledge.

## 3.4 Time belongs to the hypothesis

Markets contain activity across many horizons. A relation visible in millisecond order-book changes may be irrelevant to an hourly portfolio. A daily feature may be calculated from events that were corrected after the intended decision time. A target covering several days can overlap extensively with adjacent targets, reducing the effective independence of the sample.

For this reason, time is not merely an index. Every hypothesis defines observation time, decision time, target horizon, holding or evaluation interval where applicable, and the latency between information and permitted action. Execution adds submission, acknowledgement, fill, cancellation, and reconciliation times. Book VIII develops these clocks; Book V defines how historical experiments preserve them.

The temporal contract also limits conclusions. Evidence from one horizon does not automatically support another. A relationship that survives weekly aggregation may disappear intraday after cost. A stable average can hide state-dependent reversals. The institution seeks scope before generality.

## 3.5 Markets as networks

Instruments and venues are connected through shared participants, collateral, benchmarks, arbitrage, risk constraints, information, and execution. A strategy expressed across several symbols can represent one underlying exposure. A shock on one venue can propagate through liquidation and hedging elsewhere. Cross-sectional structure can reveal common and residual movement that a collection of isolated time series obscures.

Network language can itself become a source of overclaim. A correlation matrix is not a participant network, and a graph edge is not a mechanism. Centrality does not establish economic importance. The institution uses relational representations when the question requires them and preserves the derivation and scope of every relationship.

This matters especially for diversification. Positions can look diverse by name while relying on one shared mechanism, data source, venue, or liquidity condition. Conversely, several methods may appear similar while providing independent information under different states. Book VII treats these dependencies quantitatively. Book I establishes only the doctrine that isolation is an assumption to be tested.

## 3.6 Representation reveals and conceals

Any representation selects information. Prices preserve levels and paths; returns emphasize changes; residuals remove a specified common component; volatility scaling changes the influence of high-variance periods; ranks preserve order while discarding magnitude; event bars alter the clock; learned embeddings compress observations according to an objective and training sample.

There is no universally correct representation. Each can be appropriate to a question and harmful to another. A stationarity transform may improve compatibility with an estimator while discarding economically meaningful memory. An embedding may improve prediction while making data leakage or instability harder to diagnose. A residual may expose relative behavior while importing the assumptions of its benchmark model.

Representation therefore belongs inside the scientific claim. Chapter 9 develops the doctrine in full. At this stage, the implication is direct: apparent market structure can be a property of the observation and transformation rather than the underlying process. Alternative representations are not optional cosmetic checks; they are tests of what the conclusion depends upon.

## 3.7 Mechanism, prediction, and action

Research can produce several legitimate outputs. A descriptive result characterizes observations. A predictive result changes a conditional distribution. An explanatory result proposes why the relation occurs. A causal result supports a counterfactual or intervention claim under a defined identification strategy. A decision result recommends action under evidence, utility, and constraints.

These outputs should be linked but not collapsed. Prediction can be operationally useful without complete causal explanation. Mechanism can guide transfer and adaptation while remaining uncertain. Causal inference can strengthen intervention decisions but depends on assumptions that require criticism. Action additionally requires realizable economics, risk authority, and operational readiness.

The institution progresses by stating which kind of result it has. It does not promote correlation through a ladder of increasingly confident language. A backtest supports a scoped historical claim. Prospective observation supports a different claim. Real execution supports another. The evidence changes the object that may be asserted.

## 3.8 The continuing experiment

Markets continue producing evidence after a research report is signed. The institution monitors whether inputs, relationships, calibration, costs, capacity, execution, and mechanisms remain compatible with the approved evidence. A change does not automatically trigger retraining, reoptimization, or retirement. It triggers diagnosis under governance.

This loop prevents a false separation between research and operation while preserving their distinct authorities. Production observations return to Research Intelligence; they do not rewrite the registered hypothesis. Incidents become operational knowledge; they do not become post hoc scientific explanations. A candidate can be operationally healthy while its scientific claim weakens, or scientifically supported while its implementation fails.

Markets are therefore objects of inquiry in a precise sense. They are partially observed systems whose measurements, interactions, and evolution demand explicit representation, scope, and uncertainty. The institution does not need to declare them unsolvable. It needs to remain capable of learning when its chosen description is no longer adequate.

## Source note

This chapter revises the Founder’s Edition, Chapters 3 and 20 (pp. 24–33 and 238–251), with supporting material from Chapters 25 and 27. External claims are limited and linked to verified primary literature in the repository bibliography. Representation receives its authoritative treatment in Chapter 9; causal claim classes are developed further in Chapter 12.

