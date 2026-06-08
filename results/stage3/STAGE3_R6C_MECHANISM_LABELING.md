# R6c Stage 3 Market-Mechanism Labeling

Source Stage 2:
`C:\Users\ivanp\RL for Time-Series Forecasting\data_RLagent_for_Joseph\artifacts\stage2\R6c_root_K20_stock_K5_PD_mild_slice_group_riskaware_top8_sell12_stage2_kmeans`

Stage 1 audit:
`C:\Users\ivanp\RL for Time-Series Forecasting\data_RLagent_for_Joseph\artifacts\stage1\R6c_root_K20_stock_K5_PD_mild_slice_group_riskaware_top8_sell12_stage1_methodology_audit`

## Stage 1 Gate Reminder

```json
{
  "selected_codebook": "kmeans_K8",
  "stage1_core_gates_pass": true,
  "action_fidelity_gate_pass": false,
  "selected_beats_previous_code_action_descriptive": true,
  "selected_beats_hmm_action_descriptive": true,
  "selected_beats_market_weight_delta_descriptive": false,
  "chronological_action_fidelity_warning": "Chronological R2 remains weak; use this as a predictive/OOS caution, not as a Stage 1 descriptive-code failure.",
  "portfolio_weight_baseline_note": "portfolio_weight_kmeans may outperform hidden codes on executed weights; that is expected because it clusters the target output itself",
  "vqvae_best_k_by_recon": 32,
  "kmeans_best_k_by_recon": 128,
  "stage2_rerun_required": false,
  "decision": "Keep KMeans K=8 as primary Stage 1 codebook. Supplemental K=128 improves reconstruction but is too granular for the current interpretation layer; no Stage 2 rerun is required unless we intentionally switch codebook."
}
```

## Primitive Labels

| code_id | final_label | label_strength | method_agreement_count | top_mechanisms |
| --- | --- | --- | --- | --- |
| 0 | risk_off_deleveraging | strong | 4 | volatility_targeting:0.547; risk_off_deleveraging:0.520; forced_liquidation_stop_loss:0.510 |
| 1 | baseline_hold | strong | 3 | baseline_hold:0.554; short_term_reversal_recovery:0.532; momentum_trend_following:0.505 |
| 2 | momentum_trend_following | strong | 3 | baseline_hold:0.496; momentum_trend_following:0.488; crowding_or_concentration:0.429 |
| 3 | risk_off_deleveraging | strong | 5 | volatility_targeting:0.736; risk_off_deleveraging:0.731; liquidity_or_stress_sensitive_execution:0.654 |
| 4 | active_trading | strong | 4 | execution_metaorder_artifact:0.728; active_trading:0.705; calendar_rebalancing:0.682 |
| 5 | sector_or_group_rotation | strong | 3 | execution_metaorder_artifact:0.899; active_trading:0.805; sector_or_group_rotation:0.776 |
| 6 | baseline_hold | tentative | 2 | short_term_reversal_recovery:0.556; active_trading:0.553; sector_or_group_rotation:0.532 |
| 7 | momentum_trend_following | strong | 4 | short_term_reversal_recovery:0.838; crowding_or_concentration:0.806; momentum_trend_following:0.782 |

## Label Uncertainty

| code_id | final_label | score_margin | method_disagreement_rate | label_uncertainty | needs_manual_review |
| --- | --- | --- | --- | --- | --- |
| 0 | risk_off_deleveraging | 0.026 | 0.200 | 0.509 | False |
| 1 | baseline_hold | 0.022 | 0.400 | 0.631 | True |
| 2 | momentum_trend_following | 0.008 | 0.400 | 0.637 | True |
| 3 | risk_off_deleveraging | 0.004 | 0.000 | 0.398 | False |
| 4 | active_trading | 0.023 | 0.200 | 0.511 | False |
| 5 | sector_or_group_rotation | 0.094 | 0.400 | 0.602 | True |
| 6 | baseline_hold | 0.003 | 0.600 | 0.759 | True |
| 7 | momentum_trend_following | 0.032 | 0.200 | 0.507 | False |

## Methodology Notes

- RBSA is implemented as a local proxy because no external factor-return panel is bundled in the current artifact.
- TCAV/linear-probe is implemented as a behavior-concept proxy from logged R6c controller concepts. This is weaker than a full hidden-space TCAV run, but it is reproducible from current artifacts.
- News/LLM layer is not active because no timestamped news/event feed is present.
- `mechanism_scores.csv` keeps all mechanism evidence so labels can be revised without rerunning Stage 1/2.
