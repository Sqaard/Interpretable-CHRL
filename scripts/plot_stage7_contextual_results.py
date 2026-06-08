"""Plot Stage 7 contextual primitive replacement results.

Outputs are small README-friendly figures:
- one figure per market context showing primitive scores used for selection;
- one summary figure for Stage 7a/7b frozen-test interventions.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


DEFAULT_STAGE7_DIR = Path("results/stage7")
DEFAULT_OUT_DIR = Path("docs/assets/stage7_contextual")

LABELS = {
    0: "c0 risk-off",
    1: "c1 baseline-hold",
    2: "c2 momentum",
    3: "c3 cash-stress",
    4: "c4 active-trading",
    5: "c5 group-rotation",
    6: "c6 recovery",
    7: "c7 risk-on recovery",
}


def safe_name(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_]+", "_", str(text)).strip("_").lower()


def pp(value: float) -> float:
    return 100.0 * float(value)


def plot_context_scores(stage7_dir: Path, out_dir: Path) -> list[Path]:
    profile = pd.read_csv(stage7_dir / "stage7_primitive_context_profile.csv")
    best = pd.read_csv(stage7_dir / "stage7_context_best_map.csv")
    best_map = {str(row.market_context): int(row.selected_code_id) for row in best.itertuples(index=False)}
    outputs: list[Path] = []

    for context, g in profile.groupby("market_context", sort=True):
        g = g.sort_values("score", ascending=True).copy()
        labels = [LABELS.get(int(code), f"c{int(code)}") for code in g["code_id"]]
        selected = best_map.get(str(context))
        colors = ["#4C78A8" if int(code) != selected else "#2CA02C" for code in g["code_id"]]

        height = max(4.2, 0.46 * len(g) + 1.6)
        fig, ax = plt.subplots(figsize=(10, height))
        bars = ax.barh(labels, g["score"], color=colors, alpha=0.90)
        ax.axvline(0, color="#333333", linewidth=0.9)
        ax.set_title(f"Best Primitive for {context.replace('_', ' ').title()} Context", loc="left", fontsize=15, weight="bold")
        ax.set_xlabel("Train context score: ann. return proxy + Sharpe bonus - turnover penalty")
        ax.set_ylabel("")
        ax.grid(axis="x", color="#d9d9d9", linewidth=0.7, alpha=0.7)
        ax.set_axisbelow(True)

        for bar, (_, row) in zip(bars, g.iterrows()):
            x = float(row["score"])
            label = f"Sharpe {float(row['annualized_sharpe']):.2f} / n={int(row['n'])}"
            offset = 0.018 * max(1.0, abs(g["score"]).max())
            ha = "left" if x >= 0 else "right"
            ax.text(x + (offset if x >= 0 else -offset), bar.get_y() + bar.get_height() / 2, label, va="center", ha=ha, fontsize=9)

        note = f"Selected: {LABELS.get(selected, f'c{selected}')}  |  fitted on train split only"
        ax.text(0.0, -0.16, note, transform=ax.transAxes, fontsize=10, color="#333333")
        fig.tight_layout()
        path = out_dir / f"stage7_context_{safe_name(context)}_primitive_scores.png"
        fig.savefig(path, dpi=180, bbox_inches="tight")
        plt.close(fig)
        outputs.append(path)

    return outputs


def plot_stage7_results(stage7_dir: Path, out_dir: Path) -> Path:
    summary = pd.read_csv(stage7_dir / "stage7_counterfactual_summary.csv")
    adjusted = pd.read_csv(stage7_dir / "stage7_control_adjusted_results.csv")
    candidates = summary[
        summary["stage7_stage"].isin(["stage7a", "stage7b", "original"])
    ].copy()
    candidates = candidates[candidates["counterfactual_variant"].ne("original_ppo")]
    candidates = candidates.sort_values("delta_final_return_vs_original", ascending=False).head(12)
    adjusted = adjusted.sort_values("control_adjusted_delta_return", ascending=False).head(12)

    fig, axes = plt.subplots(1, 2, figsize=(16, 7.2))

    ax = axes[0]
    plot_df = candidates.sort_values("delta_final_return_vs_original", ascending=True)
    labels = [x.replace("stage7a_", "7a: ").replace("stage7b_", "7b: ").replace("_", " ") for x in plot_df["counterfactual_variant"]]
    colors = ["#4C78A8" if s == "stage7a" else "#F58518" for s in plot_df["stage7_stage"]]
    ax.barh(labels, plot_df["delta_final_return_vs_original"].map(pp), color=colors, alpha=0.9)
    ax.axvline(0, color="#333333", linewidth=0.9)
    ax.set_title("Stage 7 Raw Frozen-Test Lift", loc="left", fontsize=15, weight="bold")
    ax.set_xlabel("Final return lift vs original PPO, percentage points")
    ax.grid(axis="x", color="#d9d9d9", linewidth=0.7, alpha=0.7)

    ax = axes[1]
    plot_df = adjusted.sort_values("control_adjusted_delta_return", ascending=True)
    labels = [x.replace("stage7a_", "7a: ").replace("stage7b_", "7b: ").replace("_", " ") for x in plot_df["candidate"]]
    colors = ["#4C78A8" if s == "stage7a" else "#F58518" for s in plot_df["candidate_stage"]]
    ax.barh(labels, plot_df["control_adjusted_delta_return"].map(pp), color=colors, alpha=0.9)
    ax.axvline(0, color="#333333", linewidth=0.9)
    ax.set_title("Stage 7 Lift After Random-Direction Control", loc="left", fontsize=15, weight="bold")
    ax.set_xlabel("Control-adjusted final return lift, percentage points")
    ax.grid(axis="x", color="#d9d9d9", linewidth=0.7, alpha=0.7)

    fig.suptitle("Primitive Replacement vs Context-Aware Promotion", x=0.02, ha="left", fontsize=18, weight="bold")
    fig.text(
        0.02,
        0.02,
        "Blue = Stage 7a replacement. Orange = Stage 7b promotion. Evaluation: frozen 2022-2023 CHRL rollout.",
        fontsize=10,
        color="#333333",
    )
    fig.tight_layout(rect=(0, 0.04, 1, 0.95))
    path = out_dir / "stage7a_stage7b_counterfactual_results.png"
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage7-dir", type=Path, default=DEFAULT_STAGE7_DIR)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    context_paths = plot_context_scores(args.stage7_dir, args.out_dir)
    summary_path = plot_stage7_results(args.stage7_dir, args.out_dir)

    manifest = pd.DataFrame(
        [{"kind": "context", "path": str(p)} for p in context_paths]
        + [{"kind": "summary", "path": str(summary_path)}]
    )
    manifest.to_csv(args.out_dir / "stage7_plot_manifest.csv", index=False)
    print(f"Wrote {len(context_paths) + 1} Stage 7 plots to {args.out_dir}")


if __name__ == "__main__":
    main()
