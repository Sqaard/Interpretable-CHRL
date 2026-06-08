# Stage 6 Code Sanity Audit

Scope:

- `scripts/run_stage6_v2_r6c_primitive_adapter.py`
- imports from Stage 5 and Stage 5.5 runners

## Checks Passed

- Python compile passed for the Stage 6 v2 runner.
- Stage 6 v2 consumed only strict Stage 5.5 candidates.
- PPO policy body/head remained frozen; the adapter edits only exact `latent_pi`.
- Honest learned-context adapters do not receive `target_alpha` or
  `hawkes_state` as features.
- Hidden and market scalers are fit on `adapter_train` rows only.
- Source event windows inside train are split into `adapter_train` and blocked
  `adapter_holdout`; holdout pass gates are reported separately.
- Negative controls are explicit:
  - `learned_context_no_bad_penalty`
  - `learned_context_random_labels`
  - `oracle_no_bad_penalty`
- Oracle schedule adapters are labeled as baselines, not causal evidence.
- Output files were written:
  - `stage6_adapter_row_summary.csv`
  - `stage6_adapter_window_responses.csv`
  - `stage6_adapter_window_summary.csv`
  - `stage6_adapter_loss_history.csv`
  - `STAGE6_PRIMITIVE_ADAPTER_VALIDATION.md`
  - `stage6_manifest.json`
- Strict input candidate count: `2`.
- Holdout Stage 6 pass candidates: `8`.
- Holdout random-label pass candidates: `0`.
- Holdout learned no-bad pass candidates: `0`.
- Holdout oracle no-bad pass candidates: `2`.
- Holdout learned-context pass candidates: `2`.
- Holdout oracle-schedule pass candidates: `2`.

## Caveats

- This is not a counterfactual portfolio rollout.
- Official validation has no natural code-4 activations, so validation only
  checks behavior preservation, OOD, and action-shift safety.
- Oracle adapters use a Hawkes-state target derived from Stage 5.5. Honest
  learned-context adapters do not.
