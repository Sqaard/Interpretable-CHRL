# R6c Stage 2 Behavior Diagnostics

Stage 1 source:

`artifacts\stage1\R6c_root_K20_stock_K5_PD_mild_slice_group_riskaware_top8_sell12_stage1`

Rows:

- all rows: `3019`
- valid rows: `3003`
- tickers: `29`

## Stage 1 Metrics

```text
 K  best_val_recon  best_epoch  utilization  perplexity  recon_mse_normalized    var_h  recon_over_var  median_run_length  cross_fold_nmi                 source
 8        0.804561         NaN          1.0    6.913562              0.804561 1.001424        0.803417               18.0        0.633774 windowed_kmeans_vq_r6c
```

## Primitive Labels

| code_id | label | confidence | n | share_valid | rationale |
| --- | --- | --- | --- | --- | --- |
| 0 | stress | high | 527 | 0.1755 | cash=0.187, q=0.813, risk_stress=0.474, recovery=0.462, turnover=0.0017, buy_allowed=0.146 |
| 1 | baseline_hold | high | 789 | 0.2627 | cash=0.178, q=0.822, risk_stress=0.428, recovery=0.538, turnover=0.0016, buy_allowed=0.134 |
| 2 | risk_on | high | 342 | 0.1139 | cash=0.151, q=0.849, risk_stress=0.451, recovery=0.504, turnover=0.0012, buy_allowed=0.041 |
| 3 | cash_heavier+stress | high | 248 | 0.0826 | cash=0.208, q=0.792, risk_stress=0.493, recovery=0.439, turnover=0.0018, buy_allowed=0.335 |
| 4 | active_trading | high | 347 | 0.1156 | cash=0.155, q=0.845, risk_stress=0.452, recovery=0.505, turnover=0.0060, buy_allowed=0.207 |
| 5 | cash_heavier+active_trading | high | 349 | 0.1162 | cash=0.209, q=0.791, risk_stress=0.458, recovery=0.476, turnover=0.0060, buy_allowed=0.195 |
| 6 | recovery+topk_buy_open | high | 343 | 0.1142 | cash=0.205, q=0.795, risk_stress=0.414, recovery=0.553, turnover=0.0032, buy_allowed=0.440 |
| 7 | risk_on+recovery+topk_buy_open | medium | 58 | 0.0193 | cash=0.118, q=0.882, risk_stress=0.321, recovery=0.691, turnover=0.0040, buy_allowed=0.793 |

## Core Behavior Summary

| code_id | n | share_valid | median_run_length_days | mean_cash_target | mean_q_target | mean_risk_stress | mean_recovery_score | mean_confidence_rerisk | mean_confidence_derisk | mean_turnover_l1 | mean_incremental_buy_allowed | risk_break_trigger_rate | recovery_trigger_rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.0000 | 527.0000 | 0.1755 | 17.0000 | 0.1870 | 0.8130 | 0.4743 | 0.4622 | 0.3759 | 0.3919 | 0.0017 | 0.1461 | 0.0057 | 0.0019 |
| 1.0000 | 789.0000 | 0.2627 | 20.0000 | 0.1780 | 0.8220 | 0.4282 | 0.5378 | 0.4104 | 0.3459 | 0.0016 | 0.1343 | 0.0000 | 0.0025 |
| 2.0000 | 342.0000 | 0.1139 | 17.0000 | 0.1510 | 0.8490 | 0.4509 | 0.5044 | 0.3789 | 0.3683 | 0.0012 | 0.0409 | 0.0000 | 0.0000 |
| 3.0000 | 248.0000 | 0.0826 | 14.0000 | 0.2084 | 0.7916 | 0.4929 | 0.4387 | 0.4277 | 0.4365 | 0.0018 | 0.3347 | 0.0121 | 0.0161 |
| 4.0000 | 347.0000 | 0.1156 | 54.0000 | 0.1548 | 0.8452 | 0.4522 | 0.5054 | 0.4312 | 0.4118 | 0.0060 | 0.2075 | 0.0000 | 0.0029 |
| 5.0000 | 349.0000 | 0.1162 | 78.0000 | 0.2088 | 0.7912 | 0.4584 | 0.4761 | 0.5032 | 0.4790 | 0.0060 | 0.1948 | 0.0115 | 0.0057 |
| 6.0000 | 343.0000 | 0.1142 | 19.0000 | 0.2050 | 0.7950 | 0.4139 | 0.5532 | 0.5310 | 0.4050 | 0.0032 | 0.4402 | 0.0000 | 0.0262 |
| 7.0000 | 58.0000 | 0.0193 | 58.0000 | 0.1184 | 0.8816 | 0.3212 | 0.6912 | 0.6250 | 0.4123 | 0.0040 | 0.7931 | 0.0172 | 0.0862 |

## Top Tickers By Primitive

| code_id | top8_executed_weights | top8_buy_selected_rates | top8_sell_selected_rates |
| --- | --- | --- | --- |
| 0 | V:0.0328; UNH:0.0326; AMZN:0.0314; AXP:0.0312; KO:0.0308; AAPL:0.0290; JNJ:0.0287; MMM:0.0286 | CAT:0.0455; INTC:0.0455; AXP:0.0436; VZ:0.0436; V:0.0342; MRK:0.0323; CVX:0.0304; CSCO:0.0285 | V:0.3036; DIS:0.2619; AAPL:0.2334; UNH:0.2334; AMZN:0.2182; TRV:0.1992; NKE:0.1973; MSFT:0.1935 |
| 1 | V:0.0332; UNH:0.0324; AXP:0.0315; AMZN:0.0313; KO:0.0305; MMM:0.0296; JNJ:0.0291; AAPL:0.0291 | UNH:0.0570; WMT:0.0520; VZ:0.0507; MMM:0.0494; MCD:0.0456; CAT:0.0444; GS:0.0431; CVX:0.0406 | JPM:0.2738; AAPL:0.2636; AMZN:0.2522; HD:0.2459; DIS:0.2357; GS:0.2180; UNH:0.2066; CSCO:0.2003 |
| 2 | V:0.0364; UNH:0.0346; AXP:0.0334; AMZN:0.0330; WMT:0.0318; MMM:0.0317; AAPL:0.0311; JNJ:0.0310 | IBM:0.0205; TRV:0.0146; V:0.0146; AXP:0.0117; DIS:0.0117; AAPL:0.0088; CSCO:0.0088; JNJ:0.0088 | CAT:0.3830; AMZN:0.3041; BA:0.3012; INTC:0.2924; UNH:0.2895; AAPL:0.2719; JPM:0.2602; AXP:0.2398 |
| 3 | KO:0.0321; UNH:0.0315; V:0.0312; AMZN:0.0305; AXP:0.0299; JNJ:0.0285; WMT:0.0284; MCD:0.0282 | VZ:0.0726; CAT:0.0685; GS:0.0685; AMZN:0.0645; HD:0.0645; UNH:0.0605; BA:0.0484; JPM:0.0444 | JNJ:0.4073; MSFT:0.3790; UNH:0.3669; NKE:0.3629; AAPL:0.3589; KO:0.3468; MCD:0.3306; V:0.3306 |
| 4 | KO:0.0351; AXP:0.0331; UNH:0.0329; CVX:0.0306; V:0.0304; JPM:0.0294; AMZN:0.0293; DIS:0.0291 | HON:0.0951; UNH:0.0922; AXP:0.0893; CVX:0.0836; CSCO:0.0778; KO:0.0749; MCD:0.0720; MSFT:0.0692 | AXP:0.3401; AAPL:0.3343; CRM:0.3314; HD:0.3256; KO:0.3055; UNH:0.3026; IBM:0.2997; HON:0.2968 |
| 5 | UNH:0.0297; KO:0.0276; AMZN:0.0271; HD:0.0251; V:0.0242; MSFT:0.0237; JNJ:0.0237; NKE:0.0234 | MMM:0.0831; V:0.0802; INTC:0.0774; WMT:0.0745; NKE:0.0688; IBM:0.0630; MRK:0.0630; VZ:0.0630 | AAPL:0.2034; KO:0.1777; AXP:0.1748; AMZN:0.1605; CAT:0.1519; CRM:0.1433; BA:0.1318; V:0.1289 |
| 6 | UNH:0.0301; KO:0.0299; V:0.0297; AXP:0.0292; AMZN:0.0284; JNJ:0.0263; INTC:0.0262; MCD:0.0262 | GS:0.1341; CRM:0.1312; CVX:0.1224; KO:0.1224; HD:0.1137; WMT:0.1137; MMM:0.1050; AMZN:0.1020 | UNH:0.2682; TRV:0.2391; JNJ:0.2332; MSFT:0.2332; DIS:0.2303; AXP:0.2128; AAPL:0.2070; V:0.2070 |
| 7 | AMZN:0.0412; V:0.0390; UNH:0.0369; VZ:0.0344; KO:0.0343; WMT:0.0329; MSFT:0.0315; INTC:0.0310 | BA:0.5172; KO:0.4483; AXP:0.3621; VZ:0.2931; CVX:0.2759; GS:0.2586; V:0.2414; CSCO:0.2241 | AAPL:0.3793; INTC:0.3793; AMGN:0.3448; MSFT:0.3448; NKE:0.2931; VZ:0.2931; CRM:0.2586; AMZN:0.2069 |

## Codebook Comparison

                                                           main_stage1                                                             reference_stage1  overlap_rows  overlap_valid_rows  code_nmi
R6c_root_K20_stock_K5_PD_mild_slice_group_riskaware_top8_sell12_stage1 R6c_root_K20_stock_K5_PD_mild_slice_group_riskaware_top8_sell12_stage1_vqvae          3019                3003  0.490848

## Notes

For R6c, Stage 2 should be read through the hierarchy:

1. root/cash: `q_*`, `cash_*`
2. confidence/events: `risk_stress`, `recovery_score`, `confidence_*`, `risk_break_trigger`, `recovery_trigger`
3. Top-K/group-aware execution: `incremental_topk_*`
4. per-stock behavior: `trade_*`, `executed_weight_*`, `target_weight_*`

Use `stage2_primitive_behavior_summary.csv` for primitive-level interpretation
and `stage2_primitive_asset_summary.csv` for ticker-level interpretation.
