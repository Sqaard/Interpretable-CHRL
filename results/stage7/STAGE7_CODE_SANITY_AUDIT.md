# Stage 7 Code Sanity Audit

- Script: `scripts/run_stage7_r6c_contextual_primitive_replacement.py`
- Frozen fold: `fold_2021`
- Source zip: `C:\Users\ivanp\RL for Time-Series Forecasting\data_RLagent_for_Joseph\artifacts\stage0_1\R6c_root_K20_stock_K5_PD_mild_slice_group_riskaware_top8_sell12_rotation_internaldays_v1\stage0_1_job_213_R6c_v1_fold_2021_results.zip`
- PPO retrain: no.
- Environment rollout: yes, every variant calls real `env.step(action)`.
- Context-best primitive map uses train rows only.
- Frozen 2022-2023 market context uses current pre-action market features only.
- No future return, Stage 5.5 target alpha, or Hawkes state is used by Stage 7b.
- Original PPO is included as a baseline.
- Random-direction context schedule is included as a timing/control baseline.
- Output row counts: daily=12427, macro=2810, variants=43.
