import numpy as np
import pandas as pd


def generateGraphMatrix(file: str) -> tuple[np.ndarray, list[str]]:
    data = pd.read_csv(file)

    all_nodes = set(data["following"]).union(set(data["followed"]))
    node_list = sorted(all_nodes)

    node_to_index = {node: idx for idx, node in enumerate(node_list)}

    n = len(node_list)
    adjacency_matrix = np.zeros((n, n), dtype=int)

    for _, row in data.iterrows():
        following_node = row["following"]
        followed_node = row["followed"]
        i = node_to_index[following_node]
        j = node_to_index[followed_node]
        adjacency_matrix[i, j] = 1

    return adjacency_matrix, node_list


def giveMatrixB(file: str) -> np.ndarray:
    mA, _ = generateGraphMatrix(file)
    return create_matrix_B(mA)


def create_matrix_B(matrix_A: np.ndarray) -> np.ndarray:
    n = len(matrix_A)
    matrix_B = np.zeros((n, n), dtype=float)
    for i in range(n):
        matrix_B[i][i] = np.sum(matrix_A[i])
    return matrix_B


def inverse_Of_B(matrix_B) -> np.ndarray:
    n = len(matrix_B)
    for i in range(n):
        if matrix_B[i][i] != 0:
            matrix_B[i][i] = 1 / matrix_B[i][i]
    return matrix_B


def matrixBInverse(matrix_A: np.ndarray) -> np.ndarray:
    return inverse_Of_B(create_matrix_B(matrix_A))


def markovMatrix(matrix_A: np.ndarray, matrix_BInverse: np.ndarray) -> np.ndarray:
    return np.transpose(matrix_A) @ matrix_BInverse


def markovMatrixFromFile(file: str) -> tuple[np.ndarray, list[str]]:
    matrix_A, nodes = generateGraphMatrix(file)
    return markovMatrix(matrix_A, matrixBInverse(matrix_A)), nodes


if __name__ == "__main__":
    matrix_A, nodes = generateGraphMatrix("development.csv")
    print(nodes)
    matrix_BInverse = matrixBInverse(matrix_A)
    print(markovMatrix(matrix_A, matrix_BInverse))
