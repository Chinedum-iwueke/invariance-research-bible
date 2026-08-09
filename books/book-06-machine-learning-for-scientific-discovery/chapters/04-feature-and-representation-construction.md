<a id="b6-c04"></a>
# Chapter 4 — Feature and Representation Construction

Features choose which distinctions a model can express. Representation construction is therefore scientific design with the same provenance and falsification burden as model selection.

## 4.1 Representation families

Representations may encode levels, returns, differences, ranks, volatility scaling, seasonality, cross-sectional context, market state, text, graphs, or learned embeddings. A representation should correspond to a plausible information channel or a registered exploratory purpose.

More features are not automatically more information. Redundant transforms can amplify search, unstable estimation, and operational dependency.

## 4.2 Fit and transform

Every fitted transformer has a training interval, algorithm, hyperparameters, update cadence, state artifact, and output schema. Scaling, imputation, dimensionality reduction, vocabulary construction, and feature selection fit only on permitted training data. Validation and test rows use frozen state unless the registered online update policy permits otherwise.

Cross-sectional features define the point-in-time membership set. Rolling features define inclusion of the current observation. Text and alternative-data features define source publication and revision policy.

## 4.3 Learned representations

Autoencoders, contrastive objectives, sequence encoders, and foundation-model embeddings optimize surrogate objectives. Their geometry may be useful without being a mechanism. They require baselines against transparent transforms, stability across seeds and periods, ablation, nearest-neighbor inspection, probe tasks, and downstream validation.

A pretrained representation brings its pretraining corpus, objective, cutoff, license, and possible protected-evidence exposure. “Pretrained” does not mean point-in-time safe.

## 4.4 Dimensionality and regularization

Dimensionality reduction can improve conditioning or compress noise but may erase rare, decision-relevant structure. Feature selection performed repeatedly against validation outcomes belongs to model search. Regularization changes the effective hypothesis class and is tuned inside the same protected procedure as other hyperparameters.

## 4.5 Representation registry

The registry records semantic definition, producer version, source fields, temporal policy, fit state, null and unit semantics, expected range, stability checks, consumers, and known failure modes. Compatible representations are referenced by digest in Book V run contracts.

> **ML rule B6-ML04 — A latent coordinate is still a scientific claim**  
> Learned representations receive provenance, temporal controls, stability tests, and limitations even when individual dimensions lack ordinary-language names.

## Source note

This chapter develops Book I, Chapter 9 and Book IV, Chapter 3. Book V executes representation contracts; this volume owns learned construction and evaluation.
