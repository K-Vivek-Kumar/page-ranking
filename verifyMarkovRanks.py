from changes import plot_centered_bar_graph
from comparison import comparison
from markovRank import markovRank


def checkEpsilon(file: str):
    oar = markovRank(file, 1)
    ij = 1
    for i in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        pr = markovRank(file, i)
        diff = comparison(oar, pr)
        plot_centered_bar_graph(
            oar,
            diff,
            f"mRk1-vs-mRk{ij}-10.png",
            xlabel="Original Ranking Order with epsilon 1",
            ylabel="Altered Ranks from Epsilon 1",
            title=f"Original vs Epsilon {i}",
        )
        ij += 1


if __name__ == "__main__":
    inputData = "data.csv"
    checkEpsilon(inputData)
