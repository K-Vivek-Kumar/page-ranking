from authorRanks import original_authorRanks
from changes import diffTable, plot_centered_bar_graph
from complimentaryRank import complimentaryRank
from ideaRank import newIdeaRank
from weightRanks import weightedAuthorRanks


def comparison(pr, ipr):
    pr = [p[0] for p in pr]
    ipr = [ip[0] for ip in ipr]
    return diffTable(pr, ipr)


def compareWI(file: str):
    oar = weightedAuthorRanks(file)
    ir = newIdeaRank(file)
    print(ir)
    diff = comparison(oar, ir)
    plot_centered_bar_graph(
        oar,
        diff,
        "weighted-vs-idea.png",
        xlabel="Weighted Ranking Order",
        ylabel="Altered Ranks from Weighted Page Rank Algorithm",
        title="Weighted vs Context Sharing Page Rank Algorithm - Including Dangling Nodes",
    )


def compareOI(file: str):
    oar = original_authorRanks(file)
    ir = newIdeaRank(file)
    diff = comparison(oar, ir)
    plot_centered_bar_graph(
        oar,
        diff,
        "og-vs-idea.png",
        xlabel="Original Ranking Order",
        ylabel="Altered Ranks from Original Page Rank Algorithm",
        title="Original vs Our Idea Page Rank Algorithm - Including Dangling Nodes",
    )


def compareOC(file: str, takeRatio=True, alpha=0.8):
    oar = original_authorRanks(file)
    cr = complimentaryRank(file, takeRatio, alpha)
    diff = comparison(oar, cr)
    plot_centered_bar_graph(
        oar,
        diff,
        "og-vs-complimentary.png",
        xlabel="Original Ranking Order",
        ylabel="Altered Ranks from Original Page Rank Algorithm",
        title="Original vs Complimentary Graph Algorithm - Including Dangling Nodes",
    )


def compareOCDetermined(file: str, alpha=0.8):
    oar = original_authorRanks(file)
    cr = complimentaryRank(file, takeRatio=False, alpha=alpha)
    diff = comparison(oar, cr)
    plot_centered_bar_graph(
        oar,
        diff,
        f"og-vs-complimentary({alpha}).png",
        xlabel="Original Ranking Order",
        ylabel="Altered Ranks from Original Page Rank Algorithm",
        title=f"Original vs Complimentary Graph Algorithm with alpha = {alpha} - Including Dangling Nodes",
    )


def compareOW(file: str):
    oar = original_authorRanks(file)
    ir = weightedAuthorRanks(file)
    diff = comparison(oar, ir)
    plot_centered_bar_graph(
        oar,
        diff,
        "og-vs-weighted.png",
        xlabel="Original Ranking Order",
        ylabel="Altered Ranks from Original Page Rank Algorithm",
        title="Original vs Weighted Page Rank Algorithm without Dangling Nodes",
    )


def compareWC(file: str, takeRatio=True, alpha=0.8):
    oar = weightedAuthorRanks(file)
    cr = complimentaryRank(file, takeRatio, alpha)
    diff = comparison(oar, cr)
    plot_centered_bar_graph(
        oar,
        diff,
        "weighted-vs-complimentary.png",
        xlabel="Weighted Ranking Order",
        ylabel="Altered Ranks from Weighted Page Rank Algorithm",
        title="Weighted vs Complimentary Graph Algorithm - Without Dangling Nodes",
    )


if __name__ == "__main__":
    inputData = "random_authors.csv"
    # compareOC(inputData)
    compareWC(inputData)
    compareWI(inputData)
    # compareOI(inputData)
    # compareOW(inputData)
    # compareOCDetermined(inputData, alpha=0)
    # compareOCDetermined(inputData, alpha=0.1)
    # compareOCDetermined(inputData, alpha=0.2)
    # compareOCDetermined(inputData, alpha=0.3)
    # compareOCDetermined(inputData, alpha=0.4)
    # compareOCDetermined(inputData, alpha=0.5)
    # compareOCDetermined(inputData, alpha=0.6)
    # compareOCDetermined(inputData, alpha=0.7)
    # compareOCDetermined(inputData, alpha=0.8)
    # compareOCDetermined(inputData, alpha=0.9)
    # compareOCDetermined(inputData, alpha=1)
