# Stage 6b v2 Code Sanity Audit

Checks performed by construction:

- The rollout calls the real R6c `env.step(action)` for every variant.
- `original_ppo` is included as the baseline.
- Counterfactual variants edit only the frozen policy latent before the original
  policy action head.
- Learned-context current-step adapter inputs avoid post-action controller logs,
  Hawkes schedule, and Stage 5.5 target alpha.
- Frozen features are rebuilt with fold train-only scaling through 2022-2023.
- Output rows preserve daily portfolio metrics, cash, turnover, action shift,
  adapter alpha, source primitive probability, and market gate components.
- Negative controls include learned no-bad and learned random-label variants.
- Oracle/manual schedule variants are baselines, not causal learned-context
  evidence.

Run metadata:

- fold: `fold_2021`
- source zip: `C:\Users\ivanp\RL for Time-Series Forecasting\data_RLagent_for_Joseph\artifacts\stage0_1\R6c_root_K20_stock_K5_PD_mild_slice_group_riskaware_top8_sell12_rotation_internaldays_v1\stage0_1_job_213_R6c_v1_fold_2021_results.zip`
- variants: `15`
- daily rows: `4335`
- smoke test: `False`

Caveats:

- Trainable adapters are re-fit from Stage 1/4 train traces inside this runner;
  they are not PPO-retrained.
- A positive result here is still a frozen-policy counterfactual, not a newly
  trained deployable PPO policy.
