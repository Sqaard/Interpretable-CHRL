# Stage 5 One-Step Causal Audit

## Summary

This is a conservative one-step causal audit for `8` primitive codes
across `5` labeled primitive types.
It evaluates hidden-direction, hidden-subspace, and input-level interventions
using natural centroids, OOD gates, and exact policy-forward where available.

This run uses exact policy-head forward when a Stage 0 result package directory is supplied.
Hidden interventions are still one-step audits, not sequential rollouts.  Exact eligibility means:
the edited latent passes directionality, exact action-output, OOD, and immediate-risk gates and is
therefore eligible for Stage 5.5 window testing.

## Gate Decisions

| source_code | final_label | stage4_status | num_arms_tested | any_proxy_stage55_eligible | any_exact_stage55_eligible | recommended_next_step | best_proxy_arm | best_proxy_target_code | best_proxy_eta | best_proxy_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | risk_off_deleveraging | PROTECTIVE_RISK_MECHANISM | 45 | False | False | do_not_intervene | hidden_direction | 1 | 1.000 | descriptive_only_or_unsafe |
| 1 | baseline_hold | GOOD_MECHANISM | 33 | False | False | do_not_intervene | input_level | 2 | 0.250 | descriptive_only_or_unsafe |
| 2 | momentum_trend_following | GOOD_MECHANISM | 33 | True | True | eligible_for_stage55_window_audit | input_level |  | 1.000 | exact_one_step_pass |
| 3 | risk_off_deleveraging | PROTECTIVE_RISK_MECHANISM | 45 | True | True | eligible_for_stage55_window_audit | hidden_direction |  | 1.000 | exact_one_step_pass |
| 4 | active_trading | EXECUTION_ARTIFACT | 45 | True | True | eligible_for_stage55_window_audit | input_level |  | 1.000 | exact_one_step_pass |
| 5 | sector_or_group_rotation | GOOD_MECHANISM | 45 | False | False | do_not_intervene | hidden_subspace |  | 1.000 | descriptive_only_or_unsafe |
| 6 | baseline_hold | UNINTERPRETABLE | 45 | False | False | do_not_intervene | hidden_direction |  | 1.000 | descriptive_only_or_unsafe |
| 7 | momentum_trend_following | GOOD_MECHANISM | 33 | False | False | do_not_intervene | hidden_subspace |  | 0.250 | descriptive_only_or_unsafe |

## Decoder Diagnostics

| decoder | r2_in_sample | use | target_columns |
| --- | --- | --- | --- |
| hidden_to_action_mode | 0.9719 | policy_output_proxy | action_mode |
| hidden_to_raw_action_params | 1.0000 | policy_output_proxy | raw_action_params |
| hidden_to_portfolio_scalar_logs | 0.2645 | portfolio_behavior_proxy | q_target;cash_target;q_anchor;cash_anchor;q_scheduled;cash_scheduled;turnover_l1;stock_turnover_l1;concentration;risky_hhi_target;risky_entropy_target;confidence_rerisk;confidence_derisk;risk_stress;recovery_score;incremental_topk_buy_allowed;incremental_topk_buy_fill_scale;incremental_topk_rotation_requested;incremental_topk_sell_multiplier_mean |

## Policy-Forward Reproduction Diagnostics

| metric | value |
| --- | --- |
| exact_policy_forward_available | 1.000000 |
| natural_action_l1_mean | 0.000000 |
| natural_action_l1_p95 | 0.000000 |
| natural_raw_action_l2_mean | 0.000001 |
| natural_raw_action_l2_p95 | 0.000001 |
| natural_logprob_abs_diff_mean | 0.000001 |
| natural_logprob_abs_diff_p95 | 0.000008 |
| natural_entropy_abs_diff_mean | 0.000001 |
| natural_entropy_abs_diff_p95 | 0.000008 |
| reproduction_gate_pass | 1.000000 |

## Stage 4 Outcome Anchor

| code_id | final_label | status | annualized_sharpe | contribution_to_total_pnl_pct | failure_tags |
| --- | --- | --- | --- | --- | --- |
| 0 | risk_off_deleveraging | PROTECTIVE_RISK_MECHANISM | -0.2870 | -0.0476 | negative_pnl;exact_train_ppo_not_day_joined |
| 1 | baseline_hold | GOOD_MECHANISM | 3.0259 | 0.4293 | high_label_uncertainty;exact_train_ppo_not_day_joined |
| 2 | momentum_trend_following | GOOD_MECHANISM | 2.6028 | 0.1475 | high_label_uncertainty;exact_train_ppo_not_day_joined |
| 3 | risk_off_deleveraging | PROTECTIVE_RISK_MECHANISM | -0.0227 | -0.0040 | negative_pnl;exact_train_ppo_not_day_joined |
| 4 | active_trading | EXECUTION_ARTIFACT | 1.5018 | 0.1267 | high_turnover;exact_train_ppo_not_day_joined |
| 5 | sector_or_group_rotation | GOOD_MECHANISM | 1.6522 | 0.1304 | high_label_uncertainty;high_turnover;high_value_error_proxy;exact_train_ppo_not_day_joined |
| 6 | baseline_hold | UNINTERPRETABLE | 0.8433 | 0.0934 | high_label_uncertainty;exact_train_ppo_not_day_joined |
| 7 | momentum_trend_following | GOOD_MECHANISM | 2.8632 | 0.1242 | high_value_error_proxy;exact_train_ppo_not_day_joined |

## Intervention Arms Tested

| arm | source_code | target_code | eta | n | source_prob_delta_mean | target_prob_delta_mean | action_l1_shift_p95_proxy | ood_max_p95_pct | eligible_stage55_proxy | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hidden_direction | 0 |  | 0.2500 | 527 | -0.0046 |  | 0.0024 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_direction | 0 | 1 | 0.2500 | 527 | -0.0029 | 0.0036 | 0.0028 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_direction | 0 | 7 | 0.2500 | 527 | -0.0066 | 0.0007 | 0.0045 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_direction | 0 | 2 | 0.2500 | 527 | -0.0042 | 0.0056 | 0.0050 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_direction | 0 |  | 0.5000 | 527 | -0.0091 |  | 0.0047 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_direction | 0 | 1 | 0.5000 | 527 | -0.0059 | 0.0072 | 0.0055 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_direction | 0 | 7 | 0.5000 | 527 | -0.0131 | 0.0015 | 0.0091 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_direction | 0 | 2 | 0.5000 | 527 | -0.0084 | 0.0114 | 0.0100 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_direction | 0 |  | 1.0000 | 527 | -0.0181 |  | 0.0095 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_direction | 0 | 1 | 1.0000 | 527 | -0.0119 | 0.0145 | 0.0111 | 0.9500 | False | descriptive_only_or_unsafe |
| hidden_direction | 0 | 7 | 1.0000 | 527 | -0.0260 | 0.0035 | 0.0182 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_direction | 0 | 2 | 1.0000 | 527 | -0.0170 | 0.0235 | 0.0200 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_subspace | 0 |  | 0.2500 | 527 | -0.0043 |  | 0.0030 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_subspace | 0 | 1 | 0.2500 | 527 | -0.0023 | 0.0030 | 0.0040 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_subspace | 0 | 7 | 0.2500 | 527 | -0.0067 | 0.0007 | 0.0048 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_subspace | 0 | 2 | 0.2500 | 527 | -0.0038 | 0.0053 | 0.0052 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_subspace | 0 |  | 0.5000 | 527 | -0.0085 |  | 0.0059 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_subspace | 0 | 1 | 0.5000 | 527 | -0.0046 | 0.0059 | 0.0080 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_subspace | 0 | 7 | 0.5000 | 527 | -0.0133 | 0.0016 | 0.0096 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_subspace | 0 | 2 | 0.5000 | 527 | -0.0076 | 0.0108 | 0.0105 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_subspace | 0 |  | 1.0000 | 527 | -0.0170 |  | 0.0119 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_subspace | 0 | 1 | 1.0000 | 527 | -0.0095 | 0.0117 | 0.0161 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_subspace | 0 | 7 | 1.0000 | 527 | -0.0265 | 0.0037 | 0.0193 | 0.9534 | False | descriptive_only_or_unsafe |
| hidden_subspace | 0 | 2 | 1.0000 | 527 | -0.0154 | 0.0222 | 0.0210 | 0.9534 | False | descriptive_only_or_unsafe |
| input_level | 0 |  | 0.2500 | 527 | -0.0012 |  | 0.0019 | 0.9534 | False | descriptive_only_or_unsafe |
| input_level | 0 | 1 | 0.2500 | 527 | -0.0009 | 0.0009 | 0.0021 | 0.9567 | False | descriptive_only_or_unsafe |
| input_level | 0 | 7 | 0.2500 | 527 | -0.0019 | 0.0001 | 0.0046 | 0.9534 | False | descriptive_only_or_unsafe |
| input_level | 0 | 2 | 0.2500 | 527 | -0.0010 | 0.0017 | 0.0025 | 0.9567 | False | descriptive_only_or_unsafe |
| input_level | 0 |  | 0.5000 | 527 | -0.0024 |  | 0.0038 | 0.9534 | False | descriptive_only_or_unsafe |
| input_level | 0 | 1 | 0.5000 | 527 | -0.0017 | 0.0019 | 0.0042 | 0.9584 | False | descriptive_only_or_unsafe |
| input_level | 0 | 7 | 0.5000 | 527 | -0.0039 | 0.0003 | 0.0091 | 0.9534 | False | descriptive_only_or_unsafe |
| input_level | 0 | 2 | 0.5000 | 527 | -0.0020 | 0.0034 | 0.0049 | 0.9584 | False | descriptive_only_or_unsafe |
| input_level | 0 |  | 1.0000 | 527 | -0.0048 |  | 0.0075 | 0.9534 | False | descriptive_only_or_unsafe |
| input_level | 0 | 1 | 1.0000 | 527 | -0.0035 | 0.0038 | 0.0085 | 0.9590 | False | descriptive_only_or_unsafe |
| input_level | 0 | 7 | 1.0000 | 527 | -0.0079 | 0.0006 | 0.0183 | 0.9517 | False | descriptive_only_or_unsafe |
| input_level | 0 | 2 | 1.0000 | 527 | -0.0040 | 0.0068 | 0.0098 | 0.9584 | False | descriptive_only_or_unsafe |
| logit_action_mean | 0 | 1 | 0.2500 | 527 |  |  | 0.0380 |  | False | action_mean_proxy_only_not_causal_hidden_intervention |
| logit_action_mean | 0 | 7 | 0.2500 | 527 |  |  | 0.0695 |  | False | action_mean_proxy_only_not_causal_hidden_intervention |
| logit_action_mean | 0 | 2 | 0.2500 | 527 |  |  | 0.0523 |  | False | action_mean_proxy_only_not_causal_hidden_intervention |
| logit_action_mean | 0 | 1 | 0.5000 | 527 |  |  | 0.0759 |  | False | action_mean_proxy_only_not_causal_hidden_intervention |
| logit_action_mean | 0 | 7 | 0.5000 | 527 |  |  | 0.1391 |  | False | action_mean_proxy_only_not_causal_hidden_intervention |
| logit_action_mean | 0 | 2 | 0.5000 | 527 |  |  | 0.1045 |  | False | action_mean_proxy_only_not_causal_hidden_intervention |
| logit_action_mean | 0 | 1 | 1.0000 | 527 |  |  | 0.1518 |  | False | action_mean_proxy_only_not_causal_hidden_intervention |
| logit_action_mean | 0 | 7 | 1.0000 | 527 |  |  | 0.2781 |  | False | action_mean_proxy_only_not_causal_hidden_intervention |
| logit_action_mean | 0 | 2 | 1.0000 | 527 |  |  | 0.2091 |  | False | action_mean_proxy_only_not_causal_hidden_intervention |
| hidden_direction | 1 |  | 0.2500 | 789 | -0.0047 |  | 0.0016 | 0.9287 | False | descriptive_only_or_unsafe |
| hidden_direction | 1 | 7 | 0.2500 | 789 | -0.0064 | 0.0006 | 0.0032 | 0.9344 | False | descriptive_only_or_unsafe |
| hidden_direction | 1 | 2 | 0.2500 | 789 | -0.0017 | 0.0023 | 0.0027 | 0.9287 | False | descriptive_only_or_unsafe |
| hidden_direction | 1 |  | 0.5000 | 789 | -0.0094 |  | 0.0032 | 0.9327 | False | descriptive_only_or_unsafe |
| hidden_direction | 1 | 7 | 0.5000 | 789 | -0.0128 | 0.0013 | 0.0064 | 0.9397 | False | descriptive_only_or_unsafe |
| hidden_direction | 1 | 2 | 0.5000 | 789 | -0.0033 | 0.0047 | 0.0054 | 0.9317 | False | descriptive_only_or_unsafe |
| hidden_direction | 1 |  | 1.0000 | 789 | -0.0188 |  | 0.0065 | 0.9351 | False | descriptive_only_or_unsafe |
| hidden_direction | 1 | 7 | 1.0000 | 789 | -0.0259 | 0.0031 | 0.0129 | 0.9317 | False | descriptive_only_or_unsafe |
| hidden_direction | 1 | 2 | 1.0000 | 789 | -0.0067 | 0.0095 | 0.0109 | 0.9362 | False | descriptive_only_or_unsafe |
| hidden_subspace | 1 |  | 0.2500 | 789 | -0.0041 |  | 0.0024 | 0.9301 | False | descriptive_only_or_unsafe |
| hidden_subspace | 1 | 7 | 0.2500 | 789 | -0.0057 | 0.0006 | 0.0024 | 0.9344 | False | descriptive_only_or_unsafe |
| hidden_subspace | 1 | 2 | 0.2500 | 789 | -0.0003 | 0.0008 | 0.0015 | 0.9271 | False | descriptive_only_or_unsafe |
| hidden_subspace | 1 |  | 0.5000 | 789 | -0.0084 |  | 0.0048 | 0.9344 | False | descriptive_only_or_unsafe |
| hidden_subspace | 1 | 7 | 0.5000 | 789 | -0.0115 | 0.0013 | 0.0047 | 0.9397 | False | descriptive_only_or_unsafe |
| hidden_subspace | 1 | 2 | 0.5000 | 789 | -0.0005 | 0.0016 | 0.0030 | 0.9301 | False | descriptive_only_or_unsafe |

## Interpretation Contract

- `hidden_direction` and `hidden_subspace` are latent one-step interventions.
- `logit_action_mean` is an action-space proxy only; it is not a hidden causal intervention.
- `input_level` edits the replayed PPO observation and runs the full policy
  forward path (`obs -> feature extractor -> latent_pi -> action distribution`).
- `eligible_stage55_proxy=True` means the latent shift passes proxy gates.
- `eligible_stage55_exact=True` means the one-step exact policy-head gates pass. It is permission to run Stage 5.5, not a causal conclusion.
