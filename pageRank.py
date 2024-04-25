import numpy as np
import pandas as pd
from prettytable import PrettyTable

from markovMatrix import markovMatrixFromFile


def pagerank(
    markov_matrix, num_iterations=100, damping_factor=0.85, epsilon=1e-6
) -> np.ndarray:
    n = markov_matrix.shape[0]
    pr_vector = np.ones(n) / n
    for _ in range(num_iterations):
        pr_vector = (((1 - damping_factor) / n)) + (
            damping_factor * np.dot(markov_matrix, pr_vector)
        )

    return pr_vector


def showValues(nodes: list[str], page_ranks: list[float]) -> list[tuple[str, float]]:
    node_page_rank_tuples = list(zip(nodes, page_ranks))
    sorted_tuples = sorted(node_page_rank_tuples, key=lambda x: x[1], reverse=True)
    # table = PrettyTable(["Rank", "Node", "PageRank"])
    # for rank, (node, page_rank) in enumerate(sorted_tuples, start=1):
    #     table.add_row([rank, node, f"{page_rank}"])
    # print("Sorted Nodes by PageRank:")
    # print(table)
    return sorted_tuples


def display_node_out_degrees(csv_file):
    df = pd.read_csv(csv_file)
    out_degree_counts = df["following"].value_counts().to_dict()
    out_degrees = [
        (node, out_degree_counts.get(node, 0)) for node in set(df["following"])
    ]
    out_degrees = sorted(out_degrees, key=lambda x: x[1], reverse=True)
    table = PrettyTable(["Node", "Out-Degree"])
    for node, out_degree in out_degrees:
        table.add_row([node, out_degree])
    print("Node Out-Degrees:")
    print(table)


def originalPageRank(file: str) -> list[tuple[str, float]]:
    M, nodes = markovMatrixFromFile(file)
    page_ranks = pagerank(M, damping_factor=0.85)
    return showValues(nodes, page_ranks)


if __name__ == "__main__":
    inputData = "development.csv"
    inputData = "a.csv"
    M, nodes = markovMatrixFromFile(inputData)
    display_node_out_degrees(inputData)
    page_ranks = pagerank(M, damping_factor=1)
    og_pageRank = showValues(nodes, page_ranks)
