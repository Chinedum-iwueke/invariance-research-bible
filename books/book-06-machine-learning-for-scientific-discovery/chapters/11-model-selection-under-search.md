<a id="b6-c11"></a>
# Chapter 11 — Model Selection Under Search

ML performance is the output of an adaptive search over formulations, datasets, features, architectures, hyperparameters, seeds, thresholds, metrics, and stopping rules. Selection evidence must include that search.

## 11.1 Search object

Register the model family, hyperparameter domains, feature and representation alternatives, optimizer, seed policy, resource budget, proposal algorithm, early stopping, metric, tie-breaking, evidence access, and final confirmation rule. Preprocessing alternatives belong inside the search space.

## 11.2 Nested evidence

Training fits parameters. Inner validation selects hyperparameters and pipelines. Outer or protected temporal evaluation estimates the selected procedure. Reusing one validation period for repeated research still adapts the institution to that period, even when each individual run follows a clean split.

## 11.3 Seeds and variance

A lucky initialization is a trial. Report performance across registered seeds or deterministic algorithms, including failure and instability. Selecting the best seed without accounting for the choice is selection bias.

## 11.4 Multi-objective choice

Selection can consider predictive score, calibration, stability, latency, memory, turnover, interpretability, support, and cost. A predeclared rule or Pareto analysis avoids converting weights into another hidden search. Simplicity breaks near-ties when decision evidence is otherwise comparable.

## 11.5 Post-selection confirmation

After the pipeline is frozen, confirmation uses protected future or untouched environments. A disappointing result is preserved. Retraining or threshold changes after viewing confirmation create a new candidate and require new evidence.

The multiple-testing and adaptive-analysis controls of Book IV apply fully to ML. Model automation increases the number of effective trials; it does not reduce selection burden.

> **ML rule B6-ML11 — The pipeline is the selected object**  
> Evaluation targets the entire adaptive procedure that chose data transformations, features, estimator, hyperparameters, seed, calibration, and action threshold.

## Source note

This chapter operationalizes Book IV, Chapters 8–12 for ML pipelines and inherits the adaptive-analysis cautions in [Gelman and Loken 2013](../../../bibliography/references.md#gelman-loken-2013) and [Bailey and López de Prado 2014](../../../bibliography/references.md#bailey-lopez-de-prado-2014).
