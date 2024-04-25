import numpy as np
from authorRanks import normalize_columns, read_csv_data
from pageRank import showValues
from weightRanks import construct_author_matrix, weightedPageRank


def alones(matrix):
    n = matrix.shape[0]
    alone_people = []
    for i in range(n):
        if np.all(matrix[i, :] == 0):
            alone_people.append(i)
    return alone_people


def takeCompliment(matrix):
    n = matrix.shape[0]
    complement_matrix = np.zeros_like(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i, j] == 0:
                complement_matrix[i, j] = 1
                complement_matrix[j, i] = 1
            else:
                complement_matrix[i, j] = 0
                complement_matrix[j, i] = 0
    return complement_matrix


def complimentaryRank(file, takeRatio=True, alpha=0.8):
    authors_data = read_csv_data(file)
    author_matrix, authors, weights = construct_author_matrix(authors_data)
    alone_people = alones(author_matrix)
    if takeRatio:
        alpha = 1 - (len(alone_people) / len(authors))
    compliment_matrix = takeCompliment(author_matrix)
    print("Alpha taken: ", alpha)
    modified_matrix = (alpha * np.array(normalize_columns(author_matrix))) + (
        (1 - alpha) * np.array(normalize_columns(compliment_matrix))
    )
    weights = np.array(weights)
    total_weight = np.sum(weights)
    normalized_weights = weights / total_weight
    author_ranks = weightedPageRank(modified_matrix, normalized_weights)
    return showValues(authors, author_ranks)


if __name__ == "__main__":
    csv_file = "random_authors.csv"
    complimentaryRank(csv_file, takeRatio=True)
