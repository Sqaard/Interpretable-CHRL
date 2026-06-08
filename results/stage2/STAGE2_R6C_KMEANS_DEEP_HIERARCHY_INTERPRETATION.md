# R6c KMeans Deep Hierarchy Interpretation

This report reads the KMeans Stage 1 codebook through the actual R6c hierarchy:

1. root/cash layer
2. confidence and event-trigger layer
3. Top-K/risk-aware execution layer
4. rescorr group-quality layer
5. ticker routing layer

## Primitive Map

| code_id | n | hierarchy_label | root_read | confidence_read | topk_read |
| --- | --- | --- | --- | --- | --- |
| 0 | 527 | balanced / stress / buy-gate-tight / moderate | cash=0.187, q=0.813, anchor_risk=0.562, anchor_cash=0.338 | risk_stress=0.474, recovery=0.462, rerisk_conf=0.376, derisk_conf=0.392 | buy_allowed=0.146, buy_fill=0.146, sell_mult=1.303, rotation=0.00138 |
| 1 | 789 | balanced / recovery-open / buy-gate-tight / quiet | cash=0.178, q=0.822, anchor_risk=0.510, anchor_cash=0.371 | risk_stress=0.428, recovery=0.538, rerisk_conf=0.410, derisk_conf=0.346 | buy_allowed=0.134, buy_fill=0.134, sell_mult=1.274, rotation=0.00138 |
| 2 | 342 | risk-on / neutral / buy-gate-tight / quiet | cash=0.151, q=0.849, anchor_risk=0.538, anchor_cash=0.380 | risk_stress=0.451, recovery=0.504, rerisk_conf=0.379, derisk_conf=0.368 | buy_allowed=0.041, buy_fill=0.041, sell_mult=1.263, rotation=0.00131 |
| 3 | 248 | cash-heavy / stress / buy-gate-open / quiet | cash=0.208, q=0.792, anchor_risk=0.516, anchor_cash=0.444 | risk_stress=0.493, recovery=0.439, rerisk_conf=0.428, derisk_conf=0.436 | buy_allowed=0.335, buy_fill=0.335, sell_mult=1.404, rotation=0.00099 |
| 4 | 347 | risk-on / neutral / moderate-buy-gate / active | cash=0.155, q=0.845, anchor_risk=0.496, anchor_cash=0.441 | risk_stress=0.452, recovery=0.505, rerisk_conf=0.431, derisk_conf=0.412 | buy_allowed=0.207, buy_fill=0.207, sell_mult=1.310, rotation=0.00129 |
| 5 | 349 | cash-heavy / stress / moderate-buy-gate / active | cash=0.209, q=0.791, anchor_risk=0.745, anchor_cash=0.146 | risk_stress=0.458, recovery=0.476, rerisk_conf=0.503, derisk_conf=0.479 | buy_allowed=0.195, buy_fill=0.195, sell_mult=1.383, rotation=0.00177 |
| 6 | 343 | cash-heavy / recovery-open / buy-gate-open / moderate | cash=0.205, q=0.795, anchor_risk=0.612, anchor_cash=0.338 | risk_stress=0.414, recovery=0.553, rerisk_conf=0.531, derisk_conf=0.405 | buy_allowed=0.440, buy_fill=0.440, sell_mult=1.329, rotation=0.00133 |
| 7 | 58 | risk-on / recovery-open / buy-gate-open / active | cash=0.118, q=0.882, anchor_risk=0.621, anchor_cash=0.379 | risk_stress=0.321, recovery=0.691, rerisk_conf=0.625, derisk_conf=0.412 | buy_allowed=0.793, buy_fill=0.793, sell_mult=1.495, rotation=0.00144 |

## Group Routing

| code_id | dominant_buy_groups | dominant_sell_groups |
| --- | --- | --- |
| 0 | rescorr_02:0.0022; rescorr_01:0.0013; rescorr_03:0.0009 | rescorr_00:0.0014; rescorr_04:0.0011; rescorr_01:0.0009 |
| 1 | rescorr_01:0.0017; rescorr_02:0.0013; rescorr_00:0.0010 | rescorr_02:0.0012; rescorr_00:0.0011; rescorr_01:0.0005 |
| 2 | rescorr_01:0.0021; rescorr_04:0.0009; rescorr_02:0.0008 | rescorr_00:0.0014; rescorr_02:0.0013; rescorr_04:0.0003 |
| 3 | rescorr_02:0.0061; rescorr_01:0.0016; rescorr_03:0.0012 | rescorr_00:0.0027; rescorr_01:0.0024; rescorr_04:0.0016 |
| 4 | rescorr_01:0.0060; rescorr_02:0.0029; rescorr_00:0.0025 | rescorr_02:0.0023; rescorr_00:0.0021; rescorr_04:0.0004 |
| 5 | rescorr_02:0.0077; rescorr_01:0.0056; rescorr_00:0.0045 | rescorr_00:0.0020; rescorr_04:0.0017; rescorr_02:0.0007 |
| 6 | rescorr_02:0.0041; rescorr_01:0.0039; rescorr_00:0.0025 | rescorr_00:0.0019; rescorr_04:0.0011; rescorr_01:0.0010 |
| 7 | rescorr_02:0.0060; rescorr_01:0.0007; rescorr_04:0.0007 | rescorr_00:0.0041; rescorr_04:0.0009; rescorr_01:0.0007 |

## Ticker Routing

| code_id | dominant_buy_tickers | dominant_sell_tickers | dominant_executed_weights |
| --- | --- | --- | --- |
| 0 | CAT:0.0455; INTC:0.0455; AXP:0.0436; VZ:0.0436; V:0.0342; MRK:0.0323 | V:0.3036; DIS:0.2619; AAPL:0.2334; UNH:0.2334; AMZN:0.2182; TRV:0.1992 | V:0.0328; UNH:0.0326; AMZN:0.0314; AXP:0.0312; KO:0.0308; AAPL:0.0290 |
| 1 | UNH:0.0570; WMT:0.0520; VZ:0.0507; MMM:0.0494; MCD:0.0456; CAT:0.0444 | JPM:0.2738; AAPL:0.2636; AMZN:0.2522; HD:0.2459; DIS:0.2357; GS:0.2180 | V:0.0332; UNH:0.0324; AXP:0.0315; AMZN:0.0313; KO:0.0305; MMM:0.0296 |
| 2 | IBM:0.0205; TRV:0.0146; V:0.0146; AXP:0.0117; DIS:0.0117; AAPL:0.0088 | CAT:0.3830; AMZN:0.3041; BA:0.3012; INTC:0.2924; UNH:0.2895; AAPL:0.2719 | V:0.0364; UNH:0.0346; AXP:0.0334; AMZN:0.0330; WMT:0.0318; MMM:0.0317 |
| 3 | VZ:0.0726; CAT:0.0685; GS:0.0685; AMZN:0.0645; HD:0.0645; UNH:0.0605 | JNJ:0.4073; MSFT:0.3790; UNH:0.3669; NKE:0.3629; AAPL:0.3589; KO:0.3468 | KO:0.0321; UNH:0.0315; V:0.0312; AMZN:0.0305; AXP:0.0299; JNJ:0.0285 |
| 4 | HON:0.0951; UNH:0.0922; AXP:0.0893; CVX:0.0836; CSCO:0.0778; KO:0.0749 | AXP:0.3401; AAPL:0.3343; CRM:0.3314; HD:0.3256; KO:0.3055; UNH:0.3026 | KO:0.0351; AXP:0.0331; UNH:0.0329; CVX:0.0306; V:0.0304; JPM:0.0294 |
| 5 | MMM:0.0831; V:0.0802; INTC:0.0774; WMT:0.0745; NKE:0.0688; IBM:0.0630 | AAPL:0.2034; KO:0.1777; AXP:0.1748; AMZN:0.1605; CAT:0.1519; CRM:0.1433 | UNH:0.0297; KO:0.0276; AMZN:0.0271; HD:0.0251; V:0.0242; MSFT:0.0237 |
| 6 | GS:0.1341; CRM:0.1312; CVX:0.1224; KO:0.1224; HD:0.1137; WMT:0.1137 | UNH:0.2682; TRV:0.2391; JNJ:0.2332; MSFT:0.2332; DIS:0.2303; AXP:0.2128 | UNH:0.0301; KO:0.0299; V:0.0297; AXP:0.0292; AMZN:0.0284; JNJ:0.0263 |
| 7 | BA:0.5172; KO:0.4483; AXP:0.3621; VZ:0.2931; CVX:0.2759; GS:0.2586 | AAPL:0.3793; INTC:0.3793; AMGN:0.3448; MSFT:0.3448; NKE:0.2931; VZ:0.2931 | AMZN:0.0412; V:0.0390; UNH:0.0369; VZ:0.0344; KO:0.0343; WMT:0.0329 |

## Key Reading

- Codes `1` and `2` are the cleanest low-turnover risk-on/baseline regimes.
- Code `7` is the strongest recovery/re-risk primitive: low cash, high recovery score, high buy gate, concentrated in 2020 recovery.
- Codes `3`, `5`, and partly `0` are defensive/stress or cash-heavy regimes.
- Codes `4` and `5` are the active-trading regimes; they differ mainly by root cash: code `4` is risk-on active, code `5` is cash-heavy active.
- Top-K buy routing is not simply the same as executed portfolio weights. The executed book remains diversified, while Top-K logs show which names receive incremental flow.

## Generated Tables

- `stage2_level_root_cash.csv`
- `stage2_level_confidence_events.csv`
- `stage2_level_topk_execution.csv`
- `stage2_level_rescorr_groups.csv`
- `stage2_level_ticker_routes.csv`
- `stage2_deep_primitive_interpretation.csv`
