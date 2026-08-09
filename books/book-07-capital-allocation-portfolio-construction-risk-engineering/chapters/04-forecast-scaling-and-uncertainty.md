<a id="b7-c04"></a>
# Chapter 4 — Forecast Scaling and Uncertainty

Allocation requires forecasts in units related to return, risk, or utility. Scaling must preserve the meaning and uncertainty of each upstream estimate.

## 4.1 Forecast schema

Record target return or event, horizon, currency, gross or net basis, conditional population, point estimate or distribution, calibration, support, generation time, expiry, and model/data identity. Forecasts with different horizons are not added without a temporal aggregation model.

## 4.2 Calibration and shrinkage

Map model scores to realized outcomes using protected historical procedures. Because estimates are noisy, shrink toward defensible priors or zero according to evidence quality and stability. Shrinkage strength is a governed model, not a discretionary haircut applied after seeing results.

## 4.3 Uncertainty-aware scaling

Candidate exposure can depend on conservative quantiles, posterior or sampling uncertainty, forecast dispersion, or robust uncertainty sets. The mapping is bounded and monotone only where scientifically justified. Hard risk limits remain independent.

## 4.4 Aggregation

Multiple models forecasting the same object can be ensembled by fixed, performance-weighted, Bayesian, or robust schemes. Weight estimation has its own search and drift. Highly correlated models do not create independent confidence.

## 4.5 Missing and stale forecasts

Missing input triggers abstention, fallback, or constrained carry-forward under policy. Stale forecasts expire. The allocator never converts missingness to zero conviction without recording the semantic difference.

> **Risk rule B7-RK04 — Forecast precision limits capital precision**  
> Allocation does not express more confidence, horizon specificity, or support than the upstream forecast and calibration evidence justify.

## Source note

Typed uncertainty follows Book VI, Chapter 8. This chapter owns only its portfolio mapping.
