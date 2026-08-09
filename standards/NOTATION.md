# Series Notation Standard

**Status:** Controlled standard

Use ISO 8601 timestamps with explicit offsets; canonical stored time is UTC. Use SI units where applicable and state financial units explicitly. Percentages and basis points are not interchangeable: write `1%` or `100 bp` according to the object being measured.

| Symbol | Meaning |
|---|---|
| $t$ | event or observation time, as locally defined |
| $\mathcal{I}_t$ | information causally available at time $t$ |
| $x_t$ | observed or represented state at $t$ |
| $y_{t,h}$ | outcome or label over horizon $h$ |
| $r_{t,h}$ | return over horizon $h$ |
| $c_{t,h}$ | modeled cost over horizon or transaction interval |
| $\theta$ | model or strategy parameters |
| $\hat{p}$ | estimated probability |
| $\mathbb{E}$, $\operatorname{Var}$ | expectation and variance |

Vectors are bold lowercase when rendered ($\mathbf{x}$); matrices are bold uppercase ($\mathbf{X}$); sets and spaces use calligraphic capitals. Subscripts identify time, instrument, venue, or horizon in that order when several are present. Every chapter may extend this register in its book README but may not redefine a series symbol silently.

Identifiers use stable prefixes where useful (`rq_`, `hyp_`, `trial_`, `repr_`, `dataset_`, `exp_`, `run_`, `model_`, `candidate_`). An identifier names an object; a version identifies its schema or content revision; a digest establishes content identity. These roles must not be conflated.

