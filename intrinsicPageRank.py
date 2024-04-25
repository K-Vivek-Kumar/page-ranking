import pandas as pd
import numpy as np

from markovMatrix import matrixBInverse
from pageRank import pagerank, showValues


def compute_intrinsic_pagerank_matrix(adj):
    n = adj.shape[0]
    B = np.diag(np.sum(adj, axis=1))
    B_inv = matrixBInverse(B)
    A_transpose = adj.T
    I = np.eye(n)
    I_minus_B_Binv = I - (B @ B_inv)

    M = (A_transpose @ B_inv) + (((np.ones((n, n)) / n) @ I_minus_B_Binv))

    return M


def intrinsicPageRank(csv_file):
    df = pd.read_csv(csv_file)
    nodes = sorted(set(df["following"]).union(set(df["followed"])))

    n = len(nodes)
    adj_matrix = np.zeros((n, n), dtype=int)

    node_to_index = {node: idx for idx, node in enumerate(nodes)}

    for _, row in df.iterrows():
        i = node_to_index[row["following"]]
        j = node_to_index[row["followed"]]
        adj_matrix[i, j] = 1

    M = compute_intrinsic_pagerank_matrix(adj_matrix)
    page_ranks = pagerank(M, num_iterations=100, damping_factor=1)
    return showValues(nodes, page_ranks)


if __name__ == "__main__":
    csv_file_path = "development.csv"
    csv_file_path = "a.csv"

    intrinsicPageRank(csv_file_path)
