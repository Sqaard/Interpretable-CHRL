from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
RESULT_DIR = ROOT / "results" / "scientific_results"
ASSET_DIR = ROOT / "docs" / "assets" / "scientific_results"


def pp(x: float) -> float:
    return 100.0 * x


RESULT1 = [
    {
        "surface": "Hidden state",
        "candidate": "promote code4 in its own context",
        "mechanism": "contextual primitive promotion",
        "raw_return_pp": pp(0.005403582528404005),
        "delta_sharpe": 0.049159623284723196,
        "matched_control_pp": pp(0.00277792439027158),
        "control_adjusted_pp": pp(0.002625658138132425),
    },
    {
        "surface": "Hidden state",
        "candidate": "replace code3 with context-best primitive",
        "mechanism": "teacher-style primitive repair",
        "raw_return_pp": pp(0.0042074380125435296),
        "delta_sharpe": 0.03923423152439728,
        "matched_control_pp": pp(0.0011902163946808653),
        "control_adjusted_pp": pp(0.0030172216178626643),
    },
    {
        "surface": "Hidden action",
        "candidate": "learned action adapter: promote context action",
        "mechanism": "latent action primitive steering",
        "raw_return_pp": pp(0.003774906406173062),
        "delta_sharpe": 0.03554870110894663,
        "matched_control_pp": pp(0.0011281676404457652),
        "control_adjusted_pp": pp(0.002646738765727297),
    },
]


RESULT2 = [
    {
        "candidate": "hidden promote + action promote, 5-day duration",
        "type": "deployable joint intervention",
        "raw_return_pp": pp(0.004393920561307496),
        "delta_sharpe": 0.039832031470404275,
        "note": "best duration-based hidden/action combination",
    },
    {
        "candidate": "hidden promote + action promote, learned adapter",
        "type": "deployable joint adapter",
        "raw_return_pp": pp(0.004350811357271556),
        "delta_sharpe": 0.03951583770196908,
        "note": "neural adapter without target-alpha leakage",
    },
    {
        "candidate": "random-target joint control",
        "type": "control / caution",
        "raw_return_pp": pp(0.005518249756773286),
        "delta_sharpe": 0.04892701234841819,
        "note": "strong control; raw joint lift is not enough for a causal claim",
    },
]


RESULT3 = [
    {
        "candidate": "joint promote baseline",
        "role": "baseline",
        "raw_return_pp": pp(0.004293802604348862),
        "delta_sharpe": 0.04043578874478635,
        "incremental_pp": 0.0,
        "incremental_sharpe": 0.0,
    },
    {
        "candidate": "joint promote + hidden code3 repair + action code43 repair",
        "role": "real repairs",
        "raw_return_pp": pp(0.005078252612288114),
        "delta_sharpe": 0.046015842991120944,
        "incremental_pp": pp(0.0007844500079392525),
        "incremental_sharpe": 0.005580054246334593,
    },
    {
        "candidate": "joint promote + both random repairs",
        "role": "random repairs",
        "raw_return_pp": pp(0.0031582195159118864),
        "delta_sharpe": 0.030615687075382772,
        "incremental_pp": pp(-0.0011355830884369755),
        "incremental_sharpe": -0.009820101669403579,
    },
    {
        "candidate": "real repairs minus both-random repair control",
        "role": "real - random value",
        "raw_return_pp": "",
        "delta_sharpe": "",
        "incremental_pp": pp(0.001920033096376228),
        "incremental_sharpe": 0.015400155915738171,
    },
]


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def style_axes(ax, title: str, xlabel: str) -> None:
    ax.set_title(title, loc="left", fontsize=12, fontweight="bold")
    ax.set_xlabel(xlabel)
    ax.grid(axis="x", alpha=0.25)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


def plot_result1(path: Path) -> None:
    labels = [r["candidate"] for r in RESULT1]
    y = list(range(len(labels)))
    raw = [r["raw_return_pp"] for r in RESULT1]
    gap = [r["control_adjusted_pp"] for r in RESULT1]

    fig, ax = plt.subplots(figsize=(11, 4.8))
    ax.barh([v + 0.18 for v in y], raw, height=0.32, label="Raw final return lift", color="#4C78A8")
    ax.barh([v - 0.18 for v in y], gap, height=0.32, label="Matched control-adjusted lift", color="#54A24B")
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    style_axes(ax, "Result 1: controllable hidden states and hidden actions", "Final return lift vs original PPO (percentage points)")
    ax.legend(frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2)
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    fig.savefig(path, dpi=180)
    plt.close(fig)


def plot_result2(path: Path) -> None:
    labels = [r["candidate"] for r in RESULT2]
    values = [r["raw_return_pp"] for r in RESULT2]
    colors = ["#4C78A8", "#54A24B", "#F58518"]

    fig, ax = plt.subplots(figsize=(11, 4.2))
    ax.barh(labels, values, color=colors)
    ax.invert_yaxis()
    style_axes(ax, "Result 2: combining hidden-state and hidden-action control", "Final return lift vs original PPO (percentage points)")
    for i, value in enumerate(values):
        ax.text(value + 0.015, i, f"+{value:.3f} pp", va="center", fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)


def plot_result3(path: Path) -> None:
    rows = RESULT3[1:]
    labels = [r["role"] for r in rows]
    values = [r["incremental_pp"] for r in rows]
    colors = ["#54A24B" if v >= 0 else "#E45756" for v in values]

    fig, ax = plt.subplots(figsize=(11, 4.2))
    ax.axvline(0, color="#333333", linewidth=1)
    ax.barh(labels, values, color=colors)
    ax.invert_yaxis()
    style_axes(ax, "Result 3: targeted repairs improve the best joint candidate", "Incremental final return lift over joint promote baseline (percentage points)")
    for i, value in enumerate(values):
        label = f"{value:+.3f} pp"
        if value >= 0:
            ax.text(value + 0.01, i, label, va="center", ha="left", fontsize=9)
        else:
            ax.text(-0.005, i, label, va="center", ha="right", fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)


def main() -> None:
    RESULT_DIR.mkdir(parents=True, exist_ok=True)
    ASSET_DIR.mkdir(parents=True, exist_ok=True)

    write_csv(RESULT_DIR / "result1_hidden_state_action_control.csv", RESULT1)
    write_csv(RESULT_DIR / "result2_joint_hidden_action_control.csv", RESULT2)
    write_csv(RESULT_DIR / "result3_targeted_multicode_repairs.csv", RESULT3)

    plot_result1(ASSET_DIR / "result1_hidden_state_action_control.png")
    plot_result2(ASSET_DIR / "result2_joint_hidden_action_control.png")
    plot_result3(ASSET_DIR / "result3_targeted_multicode_repairs.png")


if __name__ == "__main__":
    main()
