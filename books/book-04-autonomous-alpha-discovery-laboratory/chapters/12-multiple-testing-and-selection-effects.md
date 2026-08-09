<a id="b4-c12"></a>
# Chapter 12 — Multiple Testing and Selection Effects

When the laboratory searches many questions, representations, parameters, samples, metrics, and stopping points, the best observed result is selected partly for favorable noise. Selection affects uncertainty even when every individual analysis was defensible and no one intended to manipulate evidence.

## 12.1 The selected result

Reported performance is conditional on having survived the search. Its naive estimate and interval describe the selected configuration as if it were fixed in advance, which understates uncertainty and often overstates expected performance.

The relevant family depends on the selection mechanism and scientific claim. It can include abandoned specifications, cheap screens, correlated variants, human inspections, model-generated proposals, and prior research that influenced the final design.

## 12.2 Multiplicity is not one number

Trial count is insufficient because attempts differ in dependence, objective, sample, fidelity, and visibility. A thousand near-identical parameter points and ten independent mechanisms create different selection behavior. Unexecuted forking paths can matter when analytical choices responded to observed data ([Gelman and Loken, 2013](../../../bibliography/references.md#gelman-loken-2013)).

The Trial Registry and search history preserve the actual process so methods can define an appropriate family rather than invent a convenient denominator afterward.

> **Discovery rule B4-DR12 — Selection changes evidence**  
> Every reported uncertainty and performance claim states whether the object was prespecified or selected, the relevant search family, the adjustment or validation method, and residual selection limitations.

## 12.3 Method families

Possible responses include family-wise or false-discovery control, hierarchical modeling, selective inference, nested or external evaluation, permutation or null search simulation, holdout preservation, shrinkage, and selection-adjusted performance measures. No method is universal.

Finance-specific measures can be useful within assumptions. The Deflated Sharpe Ratio, for example, was proposed to adjust Sharpe-ratio evidence for selection bias and non-normality ([Bailey and López de Prado, 2014](../../../bibliography/references.md#bailey-lopez-de-prado-2014)). It requires inputs and assumptions that must be checked; it does not transform an incomplete search history into certainty.

## 12.4 Holdouts and prospective evidence

A protected holdout provides independent evidence only to the extent that its information has not influenced adaptation. Repeated scores, rankings, or threshold decisions consume that independence. A new file name does not restore it.

Prospective shadow evidence provides temporal separation but can also become adaptive if logic changes after repeated observation. Changes start new versions and preserve prior exposure.

## 12.5 Researcher and model degrees of freedom

Human judgment, agent proposals, prompts, retrieval choices, and interpretation can expand the search beyond logged parameter sweeps. The institution records material choices without attempting comprehensive surveillance of private thought.

The durable requirement is reconstructing alternatives capable of changing the selected claim. Judgment remains necessary and becomes evidence-bearing when it adapts to results.

## 12.6 Reporting

Reports include the intended and realized search space, attempts and dependence, selection rule, protected evidence use, adjustment, sensitivity to family definition, and unadjusted versus adjusted results where helpful. Effect magnitude, cost, uncertainty, and stability remain visible alongside statistical evidence.

A corrected result can still be spurious; a result failing one conservative correction can still motivate further inquiry. The method calibrates evidence for a claim and decision rather than issuing a metaphysical verdict.

## Source note

This chapter develops Book I’s search-evidence doctrine and Book II’s registry controls using verified methodological sources. Formal method choice remains design-specific and must be implemented and tested in Books V–VI where applicable.
