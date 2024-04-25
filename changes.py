import numpy as np
from prettytable import PrettyTable
from intrinsicPageRank import intrinsicPageRank
from markovRank import markovRank
from pageRank import originalPageRank
import matplotlib.pyplot as plt


def plot_centered_bar_graph(
    categories, values, save_path=None, xlabel="", ylabel="", title=""
):
    categories = [str(cat) for cat in categories]
    categories = np.array(categories)
    values = np.array(values)
    abs_values = np.abs(values)
    if len(abs_values) > 0:
        average_deflection = np.mean(abs_values)
    else:
        average_deflection = 0
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(categories, np.maximum(values, 0), color="darkblue", align="center")
    ax.bar(categories, np.minimum(values, 0), color="lightblue", align="center")
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ranks = np.array([x for x in range(len(categories))])
    tick_positions = np.arange(len(ranks))
    show_ticks = tick_positions[:: np.maximum(len(categories) // 15, 1)]
    ax.set_xticks(show_ticks)
    ax.set_xticklabels(ranks[show_ticks])
    print(f"Average Deflection: {average_deflection:.2f}")

    legend_text = f"Average Deflection: {average_deflection:.2f}"
    ax.text(
        0.02,
        0.95,
        legend_text,
        transform=ax.transAxes,
        fontsize=10,
        verticalalignment="top",
        bbox=dict(facecolor="white", alpha=0.8),
    )

    max_abs_value = np.max(np.abs(values))
    ax.set_ylim(-max_abs_value - 1, max_abs_value + 1)
    plt.tight_layout()
    if save_path is not None:
        plt.savefig(save_path, dpi=300)
    else:
        plt.show()


def diffTable(pr: list[str], ipr: list[str]):
    diff = []
    for idx, p in enumerate(pr):
        for jdx, ip in enumerate(ipr):
            if p == ip:
                diff.append(idx - jdx)
                break
    return diff


def checkOI(file: str):
    pr: list[tuple[str, float]] = originalPageRank(file)
    ipr: list[tuple[str, float]] = intrinsicPageRank(file)
    pr = [p[0] for p in pr]
    ipr = [ip[0] for ip in ipr]
    diff = diffTable(pr, ipr)
    plot_centered_bar_graph(
        pr,
        diff,
        "og-vs-intrinsic.png",
        xlabel="Original Ranking Order",
        ylabel="Altered Ranks from Original Page Rank Algorithm",
        title="Original vs Intrinsic Page Rank Algorithm - Including Dangling Nodes",
    )


def checkIM(file: str):
    ir = intrinsicPageRank(file)
    mr = markovRank(file)
    ir = [i[0] for i in ir]
    mr = [m[0] for m in mr]
    diff = diffTable(ir, mr)
    plot_centered_bar_graph(
        ir,
        diff,
        "intrinsic-vs-markovrank.png",
        xlabel="Intrinsic Page-Rank Order",
        ylabel="Altered Ranks from Intrinsic PageRanks",
        title="Intrinsic vs MarkovRank Page Rank Algorithm - Including Dangling Nodes",
    )


def checkOM(file: str):
    pr: list[tuple[str, float]] = originalPageRank(file)
    mr = markovRank(file)
    mr = [m[0] for m in mr]
    pr = [p[0] for p in pr]
    diff = diffTable(pr, mr)
    plot_centered_bar_graph(
        pr,
        diff,
        "og-vs-markovrank.png",
        xlabel="Original Page-Rank Order",
        ylabel="Altered Ranks from Original PageRanks",
        title="Original vs MarkovRank Page Rank Algorithm - Including Dangling Nodes",
    )


if __name__ == "__main__":
    inputCSV = "data.csv"
    checkOI(inputCSV)
    checkIM(inputCSV)
    checkOM(inputCSV)
