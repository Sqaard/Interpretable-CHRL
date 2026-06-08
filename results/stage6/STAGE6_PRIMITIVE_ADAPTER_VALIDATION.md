# Stage 6 Primitive-Aware Adapter Validation

This Stage 6 v2 runner separates three ideas that were mixed in Stage 6 v1:

1. `manual_stage55_hawkes`: deterministic replay of the Stage 5.5 intervention.
2. `oracle_schedule_adapter`: an adapter allowed to see the Stage 5.5 schedule.
3. `learned_context_adapter`: the honest candidate. It does **not** see
   `target_alpha` or the Hawkes schedule and must learn from latent/context
   features plus the primitive-suppression objective.

It is still not a full counterfactual portfolio rollout and does not claim
counterfactual P&L improvement.

## Strict Stage 5.5 Inputs

| source_code | arm | length | kernel | window_type | mean_bad_auc_reduction | safe_window_rate | p95_ood_max_pct | mean_safe_suppression_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | hidden_direction | 20 | hawkes_retriggered_dose | event | 0.5682 | 1.0000 | 0.9746 | 0.5107 |
| 4 | hidden_subspace | 20 | hawkes_retriggered_dose | event | 0.5580 | 1.0000 | 0.9746 | 0.5022 |

## Event Window Results By Split

| adapter | source_code | length | window_type | split | n_windows | mean_bad_auc_reduction | safe_window_rate | p95_ood_max_pct | p95_action_l1_shift | mean_safe_suppression_score | stage6_holdout_pass_gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| learned_context_adapter_hidden_direction | 4 | 20 | event | adapter_holdout | 2 | 0.5913 | 1.0000 | 0.9763 | 0.0096 | 0.4960 | True |
| learned_context_adapter_hidden_subspace | 4 | 20 | event | adapter_holdout | 2 | 0.5805 | 1.0000 | 0.9763 | 0.0088 | 0.4872 | True |
| manual_stage55_hawkes_hidden_direction | 4 | 20 | event | adapter_holdout | 2 | 0.5396 | 1.0000 | 0.9765 | 0.0173 | 0.4469 | True |
| manual_stage55_hawkes_hidden_subspace | 4 | 20 | event | adapter_holdout | 2 | 0.5314 | 1.0000 | 0.9763 | 0.0159 | 0.4404 | True |
| oracle_schedule_adapter_hidden_direction | 4 | 20 | event | adapter_holdout | 2 | 0.1383 | 1.0000 | 0.9754 | 0.0037 | 0.0608 | True |
| oracle_no_bad_penalty_hidden_direction | 4 | 20 | event | adapter_holdout | 2 | 0.1369 | 1.0000 | 0.9754 | 0.0036 | 0.0594 | True |
| oracle_schedule_adapter_hidden_subspace | 4 | 20 | event | adapter_holdout | 2 | 0.1360 | 1.0000 | 0.9754 | 0.0034 | 0.0589 | True |
| oracle_no_bad_penalty_hidden_subspace | 4 | 20 | event | adapter_holdout | 2 | 0.1346 | 1.0000 | 0.9754 | 0.0034 | 0.0575 | True |
| learned_context_adapter_hidden_direction | 4 | 20 | event | adapter_train | 3 | 0.7262 | 1.0000 | 0.9497 | 0.0095 | 0.6887 | False |
| learned_context_adapter_hidden_subspace | 4 | 20 | event | adapter_train | 3 | 0.7102 | 1.0000 | 0.9503 | 0.0087 | 0.6737 | False |
| manual_stage55_hawkes_hidden_direction | 4 | 20 | event | adapter_train | 3 | 0.6514 | 1.0000 | 0.9497 | 0.0112 | 0.6164 | False |
| manual_stage55_hawkes_hidden_subspace | 4 | 20 | event | adapter_train | 3 | 0.6387 | 1.0000 | 0.9503 | 0.0103 | 0.6045 | False |
| oracle_schedule_adapter_hidden_direction | 4 | 20 | event | adapter_train | 3 | 0.2334 | 1.0000 | 0.9503 | 0.0040 | 0.2131 | False |
| oracle_no_bad_penalty_hidden_direction | 4 | 20 | event | adapter_train | 3 | 0.2314 | 1.0000 | 0.9503 | 0.0040 | 0.2112 | False |
| oracle_schedule_adapter_hidden_subspace | 4 | 20 | event | adapter_train | 3 | 0.2285 | 1.0000 | 0.9518 | 0.0038 | 0.2061 | False |
| oracle_no_bad_penalty_hidden_subspace | 4 | 20 | event | adapter_train | 3 | 0.2266 | 1.0000 | 0.9518 | 0.0038 | 0.2043 | False |
| learned_context_random_labels_hidden_subspace | 4 | 20 | event | adapter_train | 3 | 0.0022 | 1.0000 | 0.9518 | 0.0000 | -0.0124 | False |
| learned_context_random_labels_hidden_direction | 4 | 20 | event | adapter_train | 3 | 0.0013 | 1.0000 | 0.9518 | 0.0000 | -0.0133 | False |
| learned_context_no_bad_penalty_hidden_direction | 4 | 20 | event | adapter_train | 3 | 0.0007 | 1.0000 | 0.9518 | 0.0000 | -0.0139 | False |
| learned_context_no_bad_penalty_hidden_subspace | 4 | 20 | event | adapter_train | 3 | 0.0007 | 1.0000 | 0.9518 | 0.0000 | -0.0139 | False |
| original_ppo_hidden_direction | 4 | 20 | event | adapter_train | 3 | 0.0000 | 0.0000 | 0.9535 | 0.0000 | -0.0173 | False |
| original_ppo_hidden_subspace | 4 | 20 | event | adapter_train | 3 | 0.0000 | 0.0000 | 0.9535 | 0.0000 | -0.0173 | False |
| learned_context_random_labels_hidden_subspace | 4 | 20 | event | adapter_holdout | 2 | 0.0015 | 1.0000 | 0.9759 | 0.0000 | -0.0712 | False |
| learned_context_random_labels_hidden_direction | 4 | 20 | event | adapter_holdout | 2 | 0.0010 | 1.0000 | 0.9759 | 0.0001 | -0.0716 | False |
| learned_context_no_bad_penalty_hidden_direction | 4 | 20 | event | adapter_holdout | 2 | 0.0007 | 1.0000 | 0.9759 | 0.0000 | -0.0719 | False |
| learned_context_no_bad_penalty_hidden_subspace | 4 | 20 | event | adapter_holdout | 2 | 0.0006 | 1.0000 | 0.9759 | 0.0000 | -0.0719 | False |
| original_ppo_hidden_direction | 4 | 20 | event | adapter_holdout | 2 | 0.0000 | 0.0000 | 0.9776 | 0.0000 | -0.0767 | False |
| original_ppo_hidden_subspace | 4 | 20 | event | adapter_holdout | 2 | 0.0000 | 0.0000 | 0.9776 | 0.0000 | -0.0767 | False |

## Adapter Holdout Results

These rows are the main Stage 6 v2 check. The adapter did not train on these
blocked source windows.

| adapter | source_code | length | split | n_windows | mean_bad_auc_reduction | safe_window_rate | p95_ood_max_pct | p95_action_l1_shift | mean_safe_suppression_score | stage6_holdout_pass_gate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| learned_context_adapter_hidden_direction | 4 | 20 | adapter_holdout | 2 | 0.5913 | 1.0000 | 0.9763 | 0.0096 | 0.4960 | True |
| learned_context_adapter_hidden_subspace | 4 | 20 | adapter_holdout | 2 | 0.5805 | 1.0000 | 0.9763 | 0.0088 | 0.4872 | True |
| manual_stage55_hawkes_hidden_direction | 4 | 20 | adapter_holdout | 2 | 0.5396 | 1.0000 | 0.9765 | 0.0173 | 0.4469 | True |
| manual_stage55_hawkes_hidden_subspace | 4 | 20 | adapter_holdout | 2 | 0.5314 | 1.0000 | 0.9763 | 0.0159 | 0.4404 | True |
| oracle_schedule_adapter_hidden_direction | 4 | 20 | adapter_holdout | 2 | 0.1383 | 1.0000 | 0.9754 | 0.0037 | 0.0608 | True |
| oracle_no_bad_penalty_hidden_direction | 4 | 20 | adapter_holdout | 2 | 0.1369 | 1.0000 | 0.9754 | 0.0036 | 0.0594 | True |
| oracle_schedule_adapter_hidden_subspace | 4 | 20 | adapter_holdout | 2 | 0.1360 | 1.0000 | 0.9754 | 0.0034 | 0.0589 | True |
| oracle_no_bad_penalty_hidden_subspace | 4 | 20 | adapter_holdout | 2 | 0.1346 | 1.0000 | 0.9754 | 0.0034 | 0.0575 | True |
| learned_context_random_labels_hidden_subspace | 4 | 20 | adapter_holdout | 2 | 0.0015 | 1.0000 | 0.9759 | 0.0000 | -0.0712 | False |
| learned_context_random_labels_hidden_direction | 4 | 20 | adapter_holdout | 2 | 0.0010 | 1.0000 | 0.9759 | 0.0001 | -0.0716 | False |
| learned_context_no_bad_penalty_hidden_direction | 4 | 20 | adapter_holdout | 2 | 0.0007 | 1.0000 | 0.9759 | 0.0000 | -0.0719 | False |
| learned_context_no_bad_penalty_hidden_subspace | 4 | 20 | adapter_holdout | 2 | 0.0006 | 1.0000 | 0.9759 | 0.0000 | -0.0719 | False |
| original_ppo_hidden_direction | 4 | 20 | adapter_holdout | 2 | 0.0000 | 0.0000 | 0.9776 | 0.0000 | -0.0767 | False |
| original_ppo_hidden_subspace | 4 | 20 | adapter_holdout | 2 | 0.0000 | 0.0000 | 0.9776 | 0.0000 | -0.0767 | False |

## Official Validation Preservation

The official validation slice has no natural code-4 rows, so it can only test
behavior preservation/OOD safety, not bad-primitive suppression.

| adapter | split | n | n_source_code | mean_alpha | p95_alpha | mean_action_l1_shift | p95_action_l1_shift | p95_ood_max_pct | mean_source_prob_delta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| original_ppo_hidden_direction | validation | 243 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.9717 | 0.0000 |
| oracle_schedule_adapter_hidden_direction | validation | 243 | 0 | 0.0034 | 0.0132 | 0.0000 | 0.0001 | 0.9717 | 0.0001 |
| oracle_no_bad_penalty_hidden_direction | validation | 243 | 0 | 0.0034 | 0.0130 | 0.0000 | 0.0001 | 0.9717 | 0.0001 |
| learned_context_adapter_hidden_direction | validation | 243 | 0 | 0.0364 | 0.1425 | 0.0004 | 0.0015 | 0.9717 | 0.0008 |
| learned_context_no_bad_penalty_hidden_direction | validation | 243 | 0 | 0.0009 | 0.0010 | 0.0000 | 0.0000 | 0.9717 | 0.0000 |
| learned_context_random_labels_hidden_direction | validation | 243 | 0 | 0.0025 | 0.0068 | 0.0000 | 0.0001 | 0.9717 | 0.0000 |
| manual_stage55_hawkes_hidden_direction | validation | 243 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.9717 | 0.0000 |
| original_ppo_hidden_subspace | validation | 243 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.9717 | 0.0000 |
| oracle_schedule_adapter_hidden_subspace | validation | 243 | 0 | 0.0034 | 0.0132 | 0.0000 | 0.0001 | 0.9717 | 0.0001 |
| oracle_no_bad_penalty_hidden_subspace | validation | 243 | 0 | 0.0034 | 0.0130 | 0.0000 | 0.0001 | 0.9717 | 0.0001 |
| learned_context_adapter_hidden_subspace | validation | 243 | 0 | 0.0361 | 0.1391 | 0.0004 | 0.0014 | 0.9717 | 0.0008 |
| learned_context_no_bad_penalty_hidden_subspace | validation | 243 | 0 | 0.0009 | 0.0010 | 0.0000 | 0.0000 | 0.9717 | 0.0000 |
| learned_context_random_labels_hidden_subspace | validation | 243 | 0 | 0.0038 | 0.0063 | 0.0000 | 0.0001 | 0.9717 | 0.0001 |
| manual_stage55_hawkes_hidden_subspace | validation | 243 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.9717 | 0.0000 |

## Stage 6 Pass Candidates

| adapter | source_code | length | split | n_windows | mean_bad_auc_reduction | safe_window_rate | p95_ood_max_pct | mean_safe_suppression_score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| learned_context_adapter_hidden_direction | 4 | 20 | adapter_holdout | 2 | 0.5913 | 1.0000 | 0.9763 | 0.4960 |
| learned_context_adapter_hidden_subspace | 4 | 20 | adapter_holdout | 2 | 0.5805 | 1.0000 | 0.9763 | 0.4872 |
| manual_stage55_hawkes_hidden_direction | 4 | 20 | adapter_holdout | 2 | 0.5396 | 1.0000 | 0.9765 | 0.4469 |
| manual_stage55_hawkes_hidden_subspace | 4 | 20 | adapter_holdout | 2 | 0.5314 | 1.0000 | 0.9763 | 0.4404 |
| oracle_schedule_adapter_hidden_direction | 4 | 20 | adapter_holdout | 2 | 0.1383 | 1.0000 | 0.9754 | 0.0608 |
| oracle_no_bad_penalty_hidden_direction | 4 | 20 | adapter_holdout | 2 | 0.1369 | 1.0000 | 0.9754 | 0.0594 |
| oracle_schedule_adapter_hidden_subspace | 4 | 20 | adapter_holdout | 2 | 0.1360 | 1.0000 | 0.9754 | 0.0589 |
| oracle_no_bad_penalty_hidden_subspace | 4 | 20 | adapter_holdout | 2 | 0.1346 | 1.0000 | 0.9754 | 0.0575 |

## Control Readout

```text
holdout_random_label_pass_count       = 0
holdout_learned_no_bad_pass_count     = 0
holdout_oracle_no_bad_pass_count      = 2
holdout_oracle_schedule_pass_count    = 2
holdout_learned_context_pass_count    = 2
```

Interpretation rule:

- If `oracle_schedule_adapter` passes but `learned_context_adapter` does not,
  the Stage 5.5 schedule is useful but not yet learnable from context.
- If `learned_context_no_bad_penalty` passes, the adapter is probably just
  moving along a generally safe direction rather than suppressing the bad
  primitive specifically.
- If `oracle_no_bad_penalty` passes, that only means schedule imitation can
  work without a bad-primitive term; it is not evidence for a learned causal
  context rule.
- If `learned_context_random_labels` passes, the primitive labels are not
  specific enough for this causal claim.

## Interpretation

- `learned_context_*` rows are schedule-free learned adapters.
- `oracle_*` rows are schedule-aware baselines.
- `manual_stage55_hawkes` is the non-trainable Stage 5.5 intervention replay.

The adapter is still a latent-space validation. Stage 6b/7 must use a real
policy-forward or environment rollout before any P&L claim.

## Manifest

```json
{
  "stage": "stage6_primitive_aware_adapter_validation",
  "stage1_dir": "C:\\Users\\ivanp\\RL for Time-Series Forecasting\\data_RLagent_for_Joseph\\artifacts\\stage1\\R6c_root_K20_stock_K5_PD_mild_slice_group_riskaware_top8_sell12_stage1",
  "stage3_dir": "C:\\Users\\ivanp\\RL for Time-Series Forecasting\\data_RLagent_for_Joseph\\artifacts\\stage3\\R6c_root_K20_stock_K5_PD_mild_slice_group_riskaware_top8_sell12_stage3_kmeans",
  "stage4_dir": "C:\\Users\\ivanp\\RL for Time-Series Forecasting\\data_RLagent_for_Joseph\\artifacts\\stage4\\R6c_root_K20_stock_K5_PD_mild_slice_group_riskaware_top8_sell12_stage4_kmeans",
  "stage5_dir": "C:\\Users\\ivanp\\RL for Time-Series Forecasting\\data_RLagent_for_Joseph\\artifacts\\stage5\\R6c_root_K20_stock_K5_PD_mild_slice_group_riskaware_top8_sell12_stage5_one_step",
  "stage55_dir": "C:\\Users\\ivanp\\RL for Time-Series Forecasting\\data_RLagent_for_Joseph\\artifacts\\stage5_5\\R6c_stage55_code4_allsource_len1_3_5_10_20",
  "stage0_results_dir": "C:\\Users\\ivanp\\RL for Time-Series Forecasting\\data_RLagent_for_Joseph\\artifacts\\stage0_1\\R6c_root_K20_stock_K5_PD_mild_slice_group_riskaware_top8_sell12_rotation_internaldays_v1",
  "out_dir": "C:\\Users\\ivanp\\RL for Time-Series Forecasting\\data_RLagent_for_Joseph\\artifacts\\stage6_v2\\R6c_stage6_v2_code4_context_adapter",
  "n_rows": 3003,
  "n_strict_stage55_candidates": 2,
  "n_window_rows": 196,
  "n_window_summary_rows": 56,
  "n_stage6_event_pass_candidates": 16,
  "n_stage6_holdout_pass_candidates": 8,
  "n_random_label_holdout_pass_candidates": 0,
  "n_no_bad_penalty_holdout_pass_candidates": 2,
  "n_learned_no_bad_holdout_pass_candidates": 0,
  "n_oracle_no_bad_holdout_pass_candidates": 2,
  "n_learned_context_holdout_pass_candidates": 2,
  "n_oracle_schedule_holdout_pass_candidates": 2,
  "official_validation_source_code_4_count": 0,
  "adapter_epochs": 220,
  "adapter_lr": 0.001,
  "interpretation_contract": "stage6_v2 separates manual schedule, oracle schedule adapter, and honest context adapter; adapter validation only; no counterfactual portfolio PnL claim",
  "methodology_guards": [
    "learned_context adapters exclude target_alpha and hawkes_state",
    "scalers fit on adapter_train only",
    "blocked adapter_holdout source windows are reported separately",
    "no_bad and random_label controls are mandatory"
  ],
  "outputs": [
    "stage6_adapter_row_summary.csv",
    "stage6_adapter_window_responses.csv",
    "stage6_adapter_window_summary.csv",
    "stage6_adapter_loss_history.csv",
    "stage6_adapter_specs.csv",
    "stage6_strict_stage55_inputs.csv",
    "STAGE6_PRIMITIVE_ADAPTER_VALIDATION.md",
    "STAGE6_CODE_SANITY_AUDIT.md",
    "stage6_manifest.json"
  ]
}
```
