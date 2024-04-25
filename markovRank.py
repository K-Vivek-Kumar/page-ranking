import numpy as np
from markovMatrix import generateGraphMatrix, markovMatrix, matrixBInverse
from pageRank import pagerank, showValues


def extended(A, epsilon):
    n = A.shape[0]
    extended_matrix = np.zeros((n + 1, n + 1))
    extended_matrix[:n, :n] = A
    for i in range(n):
        extended_matrix[n, i] = epsilon * np.sum(A[i, :])
    extended_matrix[:n, n] = 1
    extended_matrix[n, n] = 0

    return extended_matrix


def markovRank(file: str, epsilon=0.5):
    adj, nodes = generateGraphMatrix(file)
    new_A = extended(adj, epsilon)
    inv_B = matrixBInverse(new_A)
    M = markovMatrix(new_A, inv_B)
    page_ranks = pagerank(M)
    return showValues(nodes, page_ranks)


if __name__ == "__main__":
    inputData = "a.csv"
    epsilon = 0.5
    markovRank(inputData, epsilon)
