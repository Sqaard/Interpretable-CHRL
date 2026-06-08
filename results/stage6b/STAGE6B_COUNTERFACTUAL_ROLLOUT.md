# Stage 6b v2 Counterfactual Portfolio Rollout

This stage applies Stage 6 v2 primitive adapters inside the frozen R6c
portfolio environment and recomputes portfolio returns via `env.step`.

## Contract

- Evaluation split: `frozen_test`.
- Fold: `fold_2021`.
- Source zip: `C:\Users\ivanp\RL for Time-Series Forecasting\data_RLagent_for_Joseph\artifacts\stage0_1\R6c_root_K20_stock_K5_PD_mild_slice_group_riskaware_top8_sell12_rotation_internaldays_v1\stage0_1_job_213_R6c_v1_fold_2021_results.zip`.
- PPO model and environment are frozen.
- Learned-context adapter inputs are pre-action only: latent, code one-hot,
  current source probability, and observable market features.
- Learned-context adapters do not receive Stage 5.5 `target_alpha` or Hawkes
  schedule.
- This stage can support a counterfactual P&L claim only if learned-context
  variants beat `original_ppo` and learned/random controls do not.

## Strict Stage 5.5 Inputs

| source_code | arm | length | kernel | window_type | mean_bad_auc_reduction | safe_window_rate | p95_ood_max_pct | mean_safe_suppression_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | hidden_direction | 20 | hawkes_retriggered_dose | event | 0.5682 | 1.0000 | 0.9746 | 0.5107 |
| 4 | hidden_subspace | 20 | hawkes_retriggered_dose | event | 0.5580 | 1.0000 | 0.9746 | 0.5022 |

## P&L Claim Readout

```text
claim_text                         = Supported as a frozen-policy env-level P&L improvement, but weak as a primitive-specific causal claim.
best_learned_context_variant        = learned_context_adapter_hidden_direction
best_learned_delta_return           = 0.001942
best_learned_delta_sharpe           = 0.015784
best_learned_no_bad_control         = learned_context_no_bad_penalty_hidden_subspace
best_learned_no_bad_delta_return    = -0.000000
best_random_label_control           = learned_context_random_labels_hidden_direction
best_random_label_delta_return      = 0.000014
best_random_direction_control       = manual_random_direction_control_hidden_subspace
best_random_direction_delta_return  = 0.001648
best_oracle_schedule_baseline       = oracle_schedule_adapter_hidden_direction
best_oracle_delta_return            = 0.001840
best_manual_stage55_baseline        = manual_stage55_hawkes_hidden_direction
best_manual_delta_return            = 0.001964
control_adjusted_learned_delta      = 0.000294
```

Interpretation:

- Env-level P&L claim: compare learned-context adapter with `original_ppo`.
- Primitive-specific causal claim: learned-context must also beat learned no-bad,
  random-label, and random-direction controls by a meaningful margin.
- Here the learned-context adapter beats original and learned controls, but the
  random-direction subspace control is close. Therefore the honest claim is
  narrow: the intervention family improves frozen-test P&L, while the exact
  primitive-specific mechanism is not yet isolated cleanly enough.

## Rollout Summary

| counterfactual_variant | n_days | final_return | annualized_sharpe | max_drawdown | mean_cash_exec | mean_turnover_l1 | mean_alpha | p95_action_l1_shift | delta_final_return_vs_original |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| manual_stage55_hawkes_hidden_direction | 289 | -0.0173 | -0.0854 | -0.1178 | 0.5053 | 0.0074 | 0.0105 | 0.0009 | 0.0020 |
| learned_context_adapter_hidden_direction | 289 | -0.0173 | -0.0857 | -0.1179 | 0.5052 | 0.0074 | 0.0584 | 0.0034 | 0.0019 |
| oracle_schedule_adapter_hidden_direction | 289 | -0.0174 | -0.0864 | -0.1179 | 0.5054 | 0.0074 | 0.0053 | 0.0001 | 0.0018 |
| oracle_no_bad_penalty_hidden_direction | 289 | -0.0174 | -0.0864 | -0.1179 | 0.5054 | 0.0074 | 0.0053 | 0.0001 | 0.0018 |
| oracle_schedule_adapter_hidden_subspace | 289 | -0.0174 | -0.0865 | -0.1179 | 0.5053 | 0.0074 | 0.0053 | 0.0001 | 0.0018 |
| oracle_no_bad_penalty_hidden_subspace | 289 | -0.0174 | -0.0865 | -0.1179 | 0.5053 | 0.0074 | 0.0053 | 0.0001 | 0.0018 |
| manual_stage55_hawkes_hidden_subspace | 289 | -0.0174 | -0.0865 | -0.1179 | 0.5053 | 0.0074 | 0.0105 | 0.0008 | 0.0018 |
| learned_context_adapter_hidden_subspace | 289 | -0.0174 | -0.0870 | -0.1179 | 0.5052 | 0.0074 | 0.0570 | 0.0031 | 0.0018 |
| manual_random_direction_control_hidden_subspace | 289 | -0.0176 | -0.0879 | -0.1179 | 0.5053 | 0.0074 | 0.0105 | 0.0011 | 0.0016 |
| learned_context_random_labels_hidden_direction | 289 | -0.0192 | -0.1014 | -0.1178 | 0.5054 | 0.0074 | 0.0076 | 0.0006 | 0.0000 |
| manual_random_direction_control_hidden_direction | 289 | -0.0192 | -0.1014 | -0.1178 | 0.5054 | 0.0074 | 0.0105 | 0.0006 | 0.0000 |
| learned_context_random_labels_hidden_subspace | 289 | -0.0192 | -0.1014 | -0.1178 | 0.5054 | 0.0074 | 0.0045 | 0.0002 | 0.0000 |
| original_ppo | 289 | -0.0192 | -0.1015 | -0.1178 | 0.5054 | 0.0074 | 0.0000 | 0.0000 | 0.0000 |
| learned_context_no_bad_penalty_hidden_subspace | 289 | -0.0192 | -0.1015 | -0.1178 | 0.5054 | 0.0074 | 0.0010 | 0.0000 | -0.0000 |
| learned_context_no_bad_penalty_hidden_direction | 289 | -0.0192 | -0.1015 | -0.1178 | 0.5054 | 0.0074 | 0.0010 | 0.0000 | -0.0000 |

## Files

- `stage6b_counterfactual_daily.csv`
- `stage6b_counterfactual_macro.csv`
- `stage6b_counterfactual_summary.csv`
- `stage6b_adapter_specs.csv`
- `stage6b_manifest.json`
- `STAGE6B_CODE_SANITY_AUDIT.md`
