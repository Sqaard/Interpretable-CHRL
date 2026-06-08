# Stage 4 Code Sanity Audit

Scope:

- `scripts/run_stage1_r6c_methodology_audit.py`
- `scripts/run_stage3_r6c_mechanism_labeling.py`
- `scripts/run_stage4_r6c_outcome_ppo_diagnostics.py`
- `scripts/run_stage4_r6c_log_ssl_deep_interpretation.py`

## Checks Passed

- Python compile passed for all Stage 1/3/4 audit scripts.
- `stage4_joined_daily.csv` has 3003 rows, all `valid == True`.
- `ppo_valid == True` for all 3003 Stage 4 rows.
- Missing key fields are all zero for:
  - `code_id`
  - `net_return`
  - `reward`
  - `ppo_logprob`
  - `ppo_entropy`
  - `ppo_value`
  - `final_label`
  - `label_uncertainty`
- All expected codes are present: 0-7.
- Daily net return sum equals primitive return-decomposition sum exactly:
  - `1.5896106833051973`
- No duplicate columns in essential Stage 4 output tables.
- Finance-safe validation p-values/q-values are in valid numeric ranges.
- R6c Stage 0.1 exact training PPO diagnostics were found and loaded from the
  original result zips:
  - `training_sample_diagnostics.csv`
  - `training_update_diagnostics.csv`
  - rollout snapshots with `advantages`, `returns`, `old_log_prob`, `old_values`
- Exact training PPO summary files were regenerated:
  - `exact_training_ppo_diagnostics_by_fold.csv`
  - `exact_training_ppo_update_diagnostics.csv`
  - `exact_training_ppo_availability.csv`
- Exact training PPO fields available by fold:
  - `approx_kl_sample`
  - `clip_indicator`
  - `advantage_raw`
  - `advantage_normalized`
  - `return`
  - `old_value`
  - `new_value`
  - `value_error`
  - `entropy`
- Deep log interpretation coverage passes:
  - 677 of 699 logged columns used for numeric SSL interpretation
  - coverage = 96.85%
  - requested 70% gate passes
- Per-log lift table has expected row count:
  - 677 selected logs * 8 codes = 5416 rows.

## Issue Found And Fixed

`classify_status()` in `scripts/run_stage4_r6c_outcome_ppo_diagnostics.py`
had a baseline persistence condition that effectively compared a return value
with itself:

```text
abs(ret) < abs(ret) + epsilon
```

That made the branch almost always true for baseline labels that reached it.
For the current R6c Stage 4 output, the main statuses were not materially
changed because good/high-uncertainty branches caught the relevant baseline
codes first. Still, the logic was wrong and could distort future runs.

It was replaced with an explicit criterion:

```text
baseline + near-zero return + low turnover => PERSISTENCE_ARTIFACT
```

## Remaining Caveats

- Exact training-time `approx_kl`, `clip_fraction`/clip indicators, and GAE
  advantages are available in Stage 0.1 training diagnostics.
- They are not joined to daily SSL primitives because R6c is an event-triggered
  K-window variant and `InstrumentedPPO` intentionally left training sample
  `date` blank. Those rows are macro-rollout training transitions, not final
  daily replay rows.
- The daily per-primitive Stage 4 table therefore still uses exact final-replay
  `entropy`, `logprob`, and `value`, plus proxy `reward_to_go`, `advantage`, and
  `value_error` fields. The exact training PPO diagnostics are reported
  separately by fold/update.
- `transaction_cost_proxy` and `factor_adjusted_alpha_proxy` are diagnostic
  proxies, not broker-exact cost/factor attribution.
