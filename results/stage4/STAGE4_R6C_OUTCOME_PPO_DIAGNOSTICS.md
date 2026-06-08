# R6c Stage 4 Outcome and PPO-Mechanism Diagnostics

Source Stage 1:
`C:\Users\ivanp\RL for Time-Series Forecasting\data_RLagent_for_Joseph\artifacts\stage1\R6c_root_K20_stock_K5_PD_mild_slice_group_riskaware_top8_sell12_stage1`

Source Stage 2:
`C:\Users\ivanp\RL for Time-Series Forecasting\data_RLagent_for_Joseph\artifacts\stage2\R6c_root_K20_stock_K5_PD_mild_slice_group_riskaware_top8_sell12_stage2_kmeans`

Source Stage 3:
`C:\Users\ivanp\RL for Time-Series Forecasting\data_RLagent_for_Joseph\artifacts\stage3\R6c_root_K20_stock_K5_PD_mild_slice_group_riskaware_top8_sell12_stage3_kmeans`

Source Stage 0.1 training diagnostics:
`C:\Users\ivanp\RL for Time-Series Forecasting\data_RLagent_for_Joseph\artifacts\stage0_1\R6c_root_K20_stock_K5_PD_mild_slice_group_riskaware_top8_sell12_rotation_internaldays_v1`

## Primitive Outcome Summary

| code_id | final_label | status | sum_one_period_return | annualized_sharpe | contribution_to_total_pnl_pct | mean_turnover_l1 | hac_t_mean_return | fdr_q_mean_return | deflated_sharpe_probability |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | risk_off_deleveraging | PROTECTIVE_RISK_MECHANISM | -0.0756 | -0.2870 | -0.0476 | 0.0017 | -0.4381 | 0.7558 | 0.0300 |
| 1 | baseline_hold | GOOD_MECHANISM | 0.6825 | 3.0259 | 0.4293 | 0.0016 | 6.3011 | 0.0000 | 0.9999 |
| 2 | momentum_trend_following | GOOD_MECHANISM | 0.2344 | 2.6028 | 0.1475 | 0.0012 | 3.4151 | 0.0026 | 0.9177 |
| 3 | risk_off_deleveraging | PROTECTIVE_RISK_MECHANISM | -0.0063 | -0.0227 | -0.0040 | 0.0018 | -0.0295 | 0.9765 | 0.0692 |
| 4 | active_trading | EXECUTION_ARTIFACT | 0.2014 | 1.5018 | 0.1267 | 0.0060 | 1.8474 | 0.1035 | 0.6171 |
| 5 | sector_or_group_rotation | GOOD_MECHANISM | 0.2073 | 1.6522 | 0.1304 | 0.0060 | 2.1549 | 0.0831 | 0.6836 |
| 6 | baseline_hold | UNINTERPRETABLE | 0.1485 | 0.8433 | 0.0934 | 0.0032 | 1.0009 | 0.4225 | 0.3187 |
| 7 | momentum_trend_following | GOOD_MECHANISM | 0.1974 | 2.8632 | 0.1242 | 0.0040 | 1.8698 | 0.1035 | 0.4621 |

## Mechanism Status

| code_id | final_label | top_mechanism | status | failure_tags |
| --- | --- | --- | --- | --- |
| 0 | risk_off_deleveraging | volatility_targeting | PROTECTIVE_RISK_MECHANISM | negative_pnl;exact_train_ppo_not_day_joined |
| 1 | baseline_hold | baseline_hold | GOOD_MECHANISM | high_label_uncertainty;exact_train_ppo_not_day_joined |
| 2 | momentum_trend_following | baseline_hold | GOOD_MECHANISM | high_label_uncertainty;exact_train_ppo_not_day_joined |
| 3 | risk_off_deleveraging | volatility_targeting | PROTECTIVE_RISK_MECHANISM | negative_pnl;exact_train_ppo_not_day_joined |
| 4 | active_trading | execution_metaorder_artifact | EXECUTION_ARTIFACT | high_turnover;exact_train_ppo_not_day_joined |
| 5 | sector_or_group_rotation | execution_metaorder_artifact | GOOD_MECHANISM | high_label_uncertainty;high_turnover;high_value_error_proxy;exact_train_ppo_not_day_joined |
| 6 | baseline_hold | short_term_reversal_recovery | UNINTERPRETABLE | high_label_uncertainty;exact_train_ppo_not_day_joined |
| 7 | momentum_trend_following | short_term_reversal_recovery | GOOD_MECHANISM | high_value_error_proxy;exact_train_ppo_not_day_joined |

## PPO Diagnostic Caveat

R6c Stage 0.1 packages contain exact training-time PPO sample diagnostics:
`approx_kl_sample`, `clip_indicator`, `advantage_raw`,
`advantage_normalized`, rollout returns, old/new values, value error, entropy,
and update-level KL/clip summaries.

However, for this event-triggered K-window variant, those PPO samples are
macro-rollout training transitions and their `date` field was intentionally
left blank by `InstrumentedPPO`. Therefore exact training PPO diagnostics are
reported separately by fold/update, not joined to daily SSL primitives.

The daily per-primitive table still uses exact final-replay entropy/logprob/
value plus transparent reward-to-go and GAE-like proxies. Do not interpret those
proxies as training-time GAE advantage.

## Exact Training PPO Diagnostics By Fold

| fold | sample_rows | mean_approx_kl_sample | mean_clip_indicator | mean_advantage_raw | std_advantage_raw | mean_abs_value_error | sample_date_nonblank |
| --- | --- | --- | --- | --- | --- | --- | --- |
| fold_2018 | 286720 | 0.0031 | 0.1552 | -0.0418 | 3.0057 | 1.6532 | 0 |
| fold_2019 | 290816 | 0.0030 | 0.1519 | -0.0699 | 2.8873 | 1.6463 | 0 |
| fold_2020 | 290816 | 0.0029 | 0.1515 | -0.0764 | 2.8914 | 1.6063 | 0 |
| fold_2021 | 290816 | 0.0030 | 0.1487 | -0.1213 | 3.1031 | 1.7570 | 0 |

## Finance-Safe Validation

This run includes block-bootstrap confidence intervals, HAC/Newey-West standard
errors for mean primitive return, Bonferroni/FDR correction across primitives,
and approximate Deflated Sharpe probabilities. Purged CV is recorded as not
applicable for this one-day-return Stage 4 table; if we evaluate overlapping
5d/10d forward outcomes, purging/embargo becomes mandatory.
