# Stage 5.5 Sequential Response Audit

## Purpose

Stage 5.5 tests whether Stage 5 one-step-eligible latent interventions remain
stable across multi-day natural windows. This is an impulse-response audit, not
a full counterfactual portfolio rollout.

## Stage 5 Arms Used

| arm | source_code | target_code | eta | n | source_prob_delta_mean | action_l1_shift_p95_exact | ood_max_p95_pct | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hidden_direction | 2 |  | 1.0000 | 342 | -0.0367 | 0.0146 | 0.9421 | exact_one_step_pass |
| hidden_subspace | 2 |  | 1.0000 | 342 | -0.0344 | 0.0131 | 0.9421 | exact_one_step_pass |
| input_level | 2 |  | 1.0000 | 342 | -0.0213 | 0.0130 | 0.9421 | exact_one_step_pass |
| hidden_direction | 3 |  | 1.0000 | 248 | -0.0305 | 0.0151 | 0.9790 | exact_one_step_pass |
| hidden_direction | 4 |  | 1.0000 | 347 | -0.0445 | 0.0108 | 0.9717 | exact_one_step_pass |
| hidden_subspace | 4 |  | 1.0000 | 347 | -0.0437 | 0.0099 | 0.9717 | exact_one_step_pass |
| input_level | 4 |  | 1.0000 | 347 | -0.0258 | 0.0105 | 0.9617 | exact_one_step_pass |

## Main Sequential Results

| source_code | arm | length | kernel | window_type | n_windows | mean_bad_auc_reduction | safe_window_rate | p95_ood_max_pct | mean_safe_suppression_score | temporal_shape_pass | stage6_candidate_strict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | hidden_direction | 20 | hawkes_retriggered_dose | event | 5 | 0.5682 | 1.0000 | 0.9746 | 0.5107 | True | True |
| 4 | hidden_subspace | 20 | hawkes_retriggered_dose | event | 5 | 0.5580 | 1.0000 | 0.9746 | 0.5022 | True | True |
| 4 | hidden_direction | 20 | constant_peak | event | 5 | 0.5265 | 1.0000 | 0.9746 | 0.4694 | True | False |
| 4 | hidden_direction | 20 | random_same_dose | event | 5 | 0.5247 | 1.0000 | 0.9750 | 0.4660 | True | False |
| 4 | hidden_direction | 20 | reverse_exponential_dose | event | 5 | 0.5213 | 1.0000 | 0.9746 | 0.4649 | True | False |
| 4 | hidden_direction | 20 | linear_dose | event | 5 | 0.5201 | 1.0000 | 0.9750 | 0.4609 | True | False |
| 4 | hidden_subspace | 20 | constant_peak | event | 5 | 0.5171 | 1.0000 | 0.9750 | 0.4601 | True | False |
| 4 | hidden_direction | 20 | raised_cosine_dose | event | 5 | 0.5175 | 1.0000 | 0.9750 | 0.4582 | True | False |
| 4 | hidden_direction | 20 | logistic_dose | event | 5 | 0.5173 | 1.0000 | 0.9750 | 0.4582 | True | False |
| 4 | hidden_subspace | 20 | reverse_exponential_dose | event | 5 | 0.5121 | 1.0000 | 0.9746 | 0.4574 | True | False |
| 4 | hidden_subspace | 20 | random_same_dose | event | 5 | 0.5129 | 1.0000 | 0.9750 | 0.4560 | True | False |
| 4 | hidden_subspace | 20 | linear_dose | event | 5 | 0.5111 | 1.0000 | 0.9750 | 0.4537 | True | False |
| 4 | hidden_direction | 20 | exponential_dose | event | 5 | 0.5122 | 1.0000 | 0.9750 | 0.4532 | True | False |
| 4 | hidden_subspace | 20 | raised_cosine_dose | event | 5 | 0.5087 | 1.0000 | 0.9750 | 0.4512 | True | False |
| 4 | hidden_direction | 20 | har_mixture_dose | event | 5 | 0.5101 | 1.0000 | 0.9750 | 0.4512 | True | False |
| 4 | hidden_subspace | 20 | logistic_dose | event | 5 | 0.5085 | 1.0000 | 0.9750 | 0.4512 | True | False |
| 4 | hidden_direction | 20 | powerlaw_dose | event | 5 | 0.5054 | 1.0000 | 0.9750 | 0.4465 | True | False |
| 4 | hidden_subspace | 20 | exponential_dose | event | 5 | 0.5036 | 1.0000 | 0.9750 | 0.4464 | True | False |
| 4 | hidden_subspace | 20 | har_mixture_dose | event | 5 | 0.5017 | 1.0000 | 0.9750 | 0.4446 | True | False |
| 2 | hidden_direction | 20 | raised_cosine_dose | event | 7 | 0.4820 | 1.0000 | 0.9640 | 0.4416 | False | False |
| 2 | hidden_direction | 20 | logistic_dose | event | 7 | 0.4819 | 1.0000 | 0.9640 | 0.4416 | False | False |
| 2 | hidden_direction | 20 | linear_dose | event | 7 | 0.4807 | 1.0000 | 0.9640 | 0.4404 | False | False |
| 4 | hidden_subspace | 20 | powerlaw_dose | event | 5 | 0.4972 | 1.0000 | 0.9750 | 0.4401 | True | False |
| 2 | hidden_direction | 20 | exponential_dose | event | 7 | 0.4803 | 1.0000 | 0.9640 | 0.4397 | False | False |
| 2 | hidden_direction | 20 | hawkes_retriggered_dose | event | 7 | 0.4750 | 1.0000 | 0.9640 | 0.4356 | False | False |

## Strict Stage 6 Candidates

| source_code | arm | length | kernel | window_type | n_windows | mean_bad_auc_reduction | safe_window_rate | p95_ood_max_pct | mean_safe_suppression_score | temporal_shape_pass |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | hidden_direction | 20 | hawkes_retriggered_dose | event | 5 | 0.5682 | 1.0000 | 0.9746 | 0.5107 | True |
| 4 | hidden_subspace | 20 | hawkes_retriggered_dose | event | 5 | 0.5580 | 1.0000 | 0.9746 | 0.5022 | True |

## Broad But Control-Weak Candidates

| source_code | arm | length | kernel | window_type | n_windows | mean_bad_auc_reduction | safe_window_rate | p95_ood_max_pct | mean_safe_suppression_score | temporal_shape_pass |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | hidden_direction | 20 | hawkes_retriggered_dose | event | 5 | 0.5682 | 1.0000 | 0.9746 | 0.5107 | True |
| 4 | hidden_subspace | 20 | hawkes_retriggered_dose | event | 5 | 0.5580 | 1.0000 | 0.9746 | 0.5022 | True |
| 4 | hidden_direction | 20 | constant_peak | event | 5 | 0.5265 | 1.0000 | 0.9746 | 0.4694 | True |
| 4 | hidden_direction | 20 | random_same_dose | event | 5 | 0.5247 | 1.0000 | 0.9750 | 0.4660 | True |
| 4 | hidden_direction | 20 | reverse_exponential_dose | event | 5 | 0.5213 | 1.0000 | 0.9746 | 0.4649 | True |
| 4 | hidden_direction | 20 | linear_dose | event | 5 | 0.5201 | 1.0000 | 0.9750 | 0.4609 | True |
| 4 | hidden_subspace | 20 | constant_peak | event | 5 | 0.5171 | 1.0000 | 0.9750 | 0.4601 | True |
| 4 | hidden_direction | 20 | raised_cosine_dose | event | 5 | 0.5175 | 1.0000 | 0.9750 | 0.4582 | True |
| 4 | hidden_direction | 20 | logistic_dose | event | 5 | 0.5173 | 1.0000 | 0.9750 | 0.4582 | True |
| 4 | hidden_subspace | 20 | reverse_exponential_dose | event | 5 | 0.5121 | 1.0000 | 0.9746 | 0.4574 | True |
| 4 | hidden_subspace | 20 | random_same_dose | event | 5 | 0.5129 | 1.0000 | 0.9750 | 0.4560 | True |
| 4 | hidden_subspace | 20 | linear_dose | event | 5 | 0.5111 | 1.0000 | 0.9750 | 0.4537 | True |
| 4 | hidden_direction | 20 | exponential_dose | event | 5 | 0.5122 | 1.0000 | 0.9750 | 0.4532 | True |
| 4 | hidden_subspace | 20 | raised_cosine_dose | event | 5 | 0.5087 | 1.0000 | 0.9750 | 0.4512 | True |
| 4 | hidden_direction | 20 | har_mixture_dose | event | 5 | 0.5101 | 1.0000 | 0.9750 | 0.4512 | True |
| 4 | hidden_subspace | 20 | logistic_dose | event | 5 | 0.5085 | 1.0000 | 0.9750 | 0.4512 | True |
| 4 | hidden_direction | 20 | powerlaw_dose | event | 5 | 0.5054 | 1.0000 | 0.9750 | 0.4465 | True |
| 4 | hidden_subspace | 20 | exponential_dose | event | 5 | 0.5036 | 1.0000 | 0.9750 | 0.4464 | True |
| 4 | hidden_subspace | 20 | har_mixture_dose | event | 5 | 0.5017 | 1.0000 | 0.9750 | 0.4446 | True |
| 2 | hidden_direction | 20 | raised_cosine_dose | event | 7 | 0.4820 | 1.0000 | 0.9640 | 0.4416 | False |
| 2 | hidden_direction | 20 | logistic_dose | event | 7 | 0.4819 | 1.0000 | 0.9640 | 0.4416 | False |
| 2 | hidden_direction | 20 | linear_dose | event | 7 | 0.4807 | 1.0000 | 0.9640 | 0.4404 | False |
| 4 | hidden_subspace | 20 | powerlaw_dose | event | 5 | 0.4972 | 1.0000 | 0.9750 | 0.4401 | True |
| 2 | hidden_direction | 20 | exponential_dose | event | 7 | 0.4803 | 1.0000 | 0.9640 | 0.4397 | False |
| 2 | hidden_direction | 20 | hawkes_retriggered_dose | event | 7 | 0.4750 | 1.0000 | 0.9640 | 0.4356 | False |

## Interpretation Contract

- Positive `mean_bad_auc_reduction` means the intervention lowered the source
  primitive probability across the window.
- `safe_window_rate` requires in-manifold OOD and non-extreme action shifts.
- `stage6_candidate_strict=True` requires safe suppression and control checks:
  exponential/decay-style intervention must beat reverse and random same-dose
  schedules, while wrong-direction must fail.
- If only the broad gate passes, the primitive is controllable but the temporal
  mechanism is not yet specific enough for Stage 6.
- `natural_cum_return` is context only. Stage 5.5 does not simulate
  counterfactual portfolio P&L.
