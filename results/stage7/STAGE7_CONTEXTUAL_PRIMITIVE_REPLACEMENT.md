# Stage 7 R6c Contextual Primitive Replacement

Stage 7 keeps PPO frozen and edits only the policy latent before the original
action head.

## Context-To-Primitive Map

The market context map is fitted on train rows only.

| market_context | selected_code_id | score | annualized_sharpe | n | selected_reason |
| --- | --- | --- | --- | --- | --- |
| bull_trend | 2 | 0.792667 | 5.035252 | 96 | train_context_score |
| calm_hold | 1 | 0.380790 | 2.244342 | 165 | train_context_score |
| choppy_rotation | 1 | 0.570492 | 3.423610 | 168 | train_context_score |
| recovery | 1 | 0.880511 | 5.504619 | 20 | train_context_score |
| stress | 7 | 1.215098 | 2.989373 | 54 | train_context_score |

## Frozen 2022-2023 Rollout Results

| counterfactual_variant | stage7_stage | stage7_mode | final_return | annualized_sharpe | delta_final_return_vs_original | delta_sharpe_vs_original | trigger_days | mean_alpha | mean_target_prob_delta |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| stage7b_promote_code4_in_own_context | stage7b | promote_dominant_context | -0.013824 | -0.052329 | 0.005404 | 0.049160 | 259 | 0.690174 | 0.006791 |
| stage7a_replace_code3_to_context_best | stage7a | replace_context_best | -0.015020 | -0.062254 | 0.004207 | 0.039234 | 122 | 0.114212 | 0.000433 |
| stage7a_replace_code3_to_global_code1 | stage7a | replace_global | -0.015312 | -0.064674 | 0.003915 | 0.036814 | 122 | 0.114213 | 0.001643 |
| stage7_control_random_promote_code3_own_context_schedule | control | random_promote_dominant_context | -0.015426 | -0.066005 | 0.003801 | 0.035483 | 147 | 0.332695 | -0.001817 |
| stage7b_promote_code5_in_own_context | stage7b | promote_dominant_context | -0.015672 | -0.067375 | 0.003555 | 0.034114 | 201 | 0.489934 | 0.004474 |
| stage7_control_random_promote_code1_own_context_schedule | control | random_promote_dominant_context | -0.015786 | -0.069476 | 0.003441 | 0.032012 | 264 | 0.664473 | -0.001297 |
| stage7a_replace_code5_to_context_best | stage7a | replace_context_best | -0.015881 | -0.074473 | 0.003347 | 0.027015 | 86 | 0.052593 | 0.000223 |
| stage7_control_random_promote_code0_own_context_schedule | control | random_promote_dominant_context | -0.016111 | -0.071913 | 0.003117 | 0.029575 | 259 | 0.633584 | 0.001213 |
| stage7b_promote_context_best | stage7b | promote_context_best | -0.016294 | -0.071166 | 0.002933 | 0.030323 | 274 | 0.760874 | 0.003929 |
| stage7b_promote_code7_in_own_context | stage7b | promote_dominant_context | -0.016303 | -0.071237 | 0.002924 | 0.030252 | 249 | 0.698268 | 0.003375 |
| stage7_control_random_replace_code5_schedule | control | random_replace_global_schedule | -0.016350 | -0.077830 | 0.002877 | 0.023658 | 86 | 0.052593 | -0.000008 |
| stage7b_promote_code0_in_own_context | stage7b | promote_dominant_context | -0.016380 | -0.072896 | 0.002847 | 0.028592 | 259 | 0.633586 | 0.005374 |
| stage7b_promote_code1_in_own_context | stage7b | promote_dominant_context | -0.016430 | -0.073267 | 0.002797 | 0.028222 | 264 | 0.664474 | 0.006708 |
| stage7_control_random_promote_code4_own_context_schedule | control | random_promote_dominant_context | -0.016449 | -0.074642 | 0.002778 | 0.026846 | 259 | 0.690177 | 0.001490 |
| stage7b_promote_code6_in_own_context | stage7b | promote_dominant_context | -0.016785 | -0.076258 | 0.002442 | 0.025231 | 205 | 0.493583 | 0.004195 |
| stage7_control_random_promote_code5_own_context_schedule | control | random_promote_dominant_context | -0.016903 | -0.078477 | 0.002324 | 0.023011 | 201 | 0.489932 | 0.001385 |
| stage7_control_random_direction_context_best_schedule | control | random_context_schedule | -0.016922 | -0.083306 | 0.002305 | 0.018182 | 279 | 0.778894 | 0.000510 |
| stage7_control_random_promote_code7_own_context_schedule | control | random_promote_dominant_context | -0.016955 | -0.082602 | 0.002272 | 0.018886 | 254 | 0.716286 | 0.000015 |
| stage7b_promote_code3_in_own_context | stage7b | promote_dominant_context | -0.017050 | -0.079124 | 0.002177 | 0.022365 | 147 | 0.332695 | 0.003516 |
| stage7a_replace_code6_to_context_best | stage7a | replace_context_best | -0.017162 | -0.084429 | 0.002066 | 0.017059 | 56 | 0.036139 | 0.000422 |
| stage7a_replace_code4_to_global_code1 | stage7a | replace_global | -0.017396 | -0.086499 | 0.001831 | 0.014989 | 5 | 0.003338 | 0.000047 |
| stage7_control_random_replace_code7_schedule | control | random_replace_global_schedule | -0.017397 | -0.086499 | 0.001830 | 0.014989 | 10 | 0.010670 | -0.000025 |
| stage7_control_random_promote_code6_own_context_schedule | control | random_promote_dominant_context | -0.017606 | -0.088402 | 0.001622 | 0.013086 | 208 | 0.496099 | 0.001886 |
| stage7_control_random_replace_code6_schedule | control | random_replace_global_schedule | -0.017795 | -0.089680 | 0.001433 | 0.011808 | 56 | 0.036139 | -0.000027 |
| stage7a_replace_code5_to_global_code1 | stage7a | replace_global | -0.017885 | -0.090414 | 0.001342 | 0.011074 | 86 | 0.052593 | 0.000783 |
| stage7a_replace_code7_to_global_code1 | stage7a | replace_global | -0.017965 | -0.091202 | 0.001262 | 0.010287 | 10 | 0.010670 | 0.000178 |
| stage7a_replace_code6_to_global_code1 | stage7a | replace_global | -0.018036 | -0.091739 | 0.001191 | 0.009749 | 56 | 0.036139 | 0.000597 |
| stage7_control_random_replace_code3_schedule | control | random_replace_global_schedule | -0.018037 | -0.091770 | 0.001190 | 0.009718 | 122 | 0.114213 | 0.000132 |
| stage7a_replace_code0_to_context_best | stage7a | replace_context_best | -0.019224 | -0.101465 | 0.000003 | 0.000023 | 10 | 0.005593 | 0.000035 |
| stage7a_replace_code0_to_global_code1 | stage7a | replace_global | -0.019226 | -0.101477 | 0.000001 | 0.000012 | 10 | 0.005593 | 0.000066 |
| stage7_control_random_replace_code4_schedule | control | random_replace_global_schedule | -0.019227 | -0.101486 | 0.000000 | 0.000002 | 5 | 0.003338 | -0.000003 |
| original_ppo | original | none | -0.019227 | -0.101488 | 0.000000 | 0.000000 | 0 | 0.000000 |  |
| stage7_control_random_promote_code2_own_context_schedule | control | random_promote_dominant_context | -0.019227 | -0.101488 | 0.000000 | 0.000000 | 0 | 0.000000 | 0.000000 |
| stage7_control_random_replace_code1_schedule | control | random_replace_global_schedule | -0.019227 | -0.101488 | 0.000000 | 0.000000 | 0 | 0.000000 | 0.000000 |
| stage7_control_random_replace_code2_schedule | control | random_replace_global_schedule | -0.019227 | -0.101488 | 0.000000 | 0.000000 | 0 | 0.000000 | 0.000000 |
| stage7a_replace_code1_to_context_best | stage7a | replace_context_best | -0.019227 | -0.101488 | 0.000000 | 0.000000 | 0 | 0.000000 | 0.000000 |
| stage7a_replace_code1_to_global_code7 | stage7a | replace_global | -0.019227 | -0.101488 | 0.000000 | 0.000000 | 0 | 0.000000 | 0.000000 |
| stage7a_replace_code2_to_context_best | stage7a | replace_context_best | -0.019227 | -0.101488 | 0.000000 | 0.000000 | 0 | 0.000000 | 0.000000 |
| stage7a_replace_code2_to_global_code1 | stage7a | replace_global | -0.019227 | -0.101488 | 0.000000 | 0.000000 | 0 | 0.000000 | 0.000000 |
| stage7a_replace_code7_to_context_best | stage7a | replace_context_best | -0.019227 | -0.101488 | 0.000000 | 0.000000 | 0 | 0.000000 | 0.000000 |

## Control-Adjusted Results

| candidate | control_adjusted_delta_return | candidate_delta_return | control_delta_return | control_adjusted_delta_sharpe | candidate_trigger_days | control_trigger_days |
| --- | --- | --- | --- | --- | --- | --- |
| stage7a_replace_code3_to_context_best | 0.003017 | 0.004207 | 0.001190 | 0.029516 | 122 | 122 |
| stage7a_replace_code3_to_global_code1 | 0.002725 | 0.003915 | 0.001190 | 0.027096 | 122 | 122 |
| stage7b_promote_code4_in_own_context | 0.002626 | 0.005404 | 0.002778 | 0.022314 | 259 | 259 |
| stage7a_replace_code4_to_global_code1 | 0.001831 | 0.001831 | 0.000000 | 0.014987 | 5 | 5 |
| stage7b_promote_code5_in_own_context | 0.001231 | 0.003555 | 0.002324 | 0.011103 | 201 | 201 |
| stage7b_promote_code6_in_own_context | 0.000821 | 0.002442 | 0.001622 | 0.012144 | 205 | 208 |
| stage7b_promote_code7_in_own_context | 0.000652 | 0.002924 | 0.002272 | 0.011366 | 249 | 254 |
| stage7a_replace_code6_to_context_best | 0.000633 | 0.002066 | 0.001433 | 0.005251 | 56 | 56 |
| stage7b_promote_context_best | 0.000629 | 0.002933 | 0.002305 | 0.012140 | 274 | 279 |
| stage7a_replace_code5_to_context_best | 0.000470 | 0.003347 | 0.002877 | 0.003357 | 86 | 86 |
| stage7a_replace_code0_to_context_best | 0.000004 | 0.000003 | -0.000001 | 0.000032 | 10 | 10 |
| stage7a_replace_code0_to_global_code1 | 0.000003 | 0.000001 | -0.000001 | 0.000020 | 10 | 10 |
| stage7a_replace_code1_to_context_best | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0 | 0 |
| stage7a_replace_code1_to_global_code7 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0 | 0 |
| stage7a_replace_code2_to_context_best | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0 | 0 |
| stage7a_replace_code2_to_global_code1 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0 | 0 |
| stage7b_promote_code2_in_own_context | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0 | 0 |
| stage7a_replace_code4_to_context_best | -0.000009 | -0.000009 | 0.000000 | -0.000067 | 5 | 5 |
| stage7a_replace_code6_to_global_code1 | -0.000242 | 0.001191 | 0.001433 | -0.002059 | 56 | 56 |
| stage7b_promote_code0_in_own_context | -0.000270 | 0.002847 | 0.003117 | -0.000983 | 259 | 259 |
| stage7a_replace_code7_to_global_code1 | -0.000568 | 0.001262 | 0.001830 | -0.004702 | 10 | 10 |
| stage7b_promote_code1_in_own_context | -0.000645 | 0.002797 | 0.003441 | -0.003790 | 264 | 264 |
| stage7a_replace_code5_to_global_code1 | -0.001535 | 0.001342 | 0.002877 | -0.012584 | 86 | 86 |
| stage7b_promote_code3_in_own_context | -0.001624 | 0.002177 | 0.003801 | -0.013119 | 147 | 147 |
| stage7a_replace_code7_to_context_best | -0.001830 | 0.000000 | 0.001830 | -0.014989 | 0 | 10 |

## Interpretation

- `stage7a` asks whether a source primitive should be replaced by a globally
  better primitive, or by the train-best primitive for the current context.
- `stage7b` asks whether the model benefits from promoting the train-best
  primitive for the current context, even when the natural primitive is not
  obviously bad.
- The random-direction context schedule is a control for timing/context effects.
  A candidate is stronger only if it beats original PPO and the random control.

## Methodology Guards

- PPO and environment are frozen
- every candidate is evaluated through real env.step
- context-best primitive mapping is train-only
- frozen rollout uses only current pre-action hidden and market features
- Stage 7 does not use future returns, target alpha, or Stage 5.5 schedules
- random-direction context schedule control is included
