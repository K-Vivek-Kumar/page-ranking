from collections import defaultdict
import numpy as np

from authorRanks import (
    construct_author_matrix,
    normalize_columns,
    read_csv_data,
)
from pageRank import showValues


def weightedPageRank(
    markov_matrix, weight_matrix, num_iterations=100, damping_factor=0.85, epsilon=1e-6
) -> np.ndarray:
    n = markov_matrix.shape[0]
    pr_vector = np.ones(n) / n
    for _ in range(num_iterations):
        pr_vector = ((1 - damping_factor) * weight_matrix) + (
            damping_factor * np.dot(markov_matrix, pr_vector)
        )

    return pr_vector


def construct_author_matrix(authors_data):
    unique_authors = list(set([author for row in authors_data for author in row]))
    author_to_row_count = defaultdict(int)
    total_rows = len(unique_authors)
    author_matrix = np.zeros((total_rows, total_rows), dtype=int)
    for row in authors_data:
        authors_set = set(row)
        for author in authors_set:
            author_to_row_count[author] += 1
        for j in range(len(row)):
            for k in range(j + 1, len(row)):
                r = unique_authors.index(row[j])
                c = unique_authors.index(row[k])
                author_matrix[r][c] += 1
                author_matrix[c][r] += 1
    author_publication_counts = [
        author_to_row_count[author] for author in unique_authors
    ]

    return author_matrix, unique_authors, author_publication_counts


def weightedAuthorRanks(file: str):
    authors_data = read_csv_data(file)
    author_matrix, authors, weights = construct_author_matrix(authors_data)
    weights = np.array(weights)
    if weights.sum() > 0:
        normalized_weights = weights / weights.sum()
    else:
        normalized_weights = weights
    normalized = normalize_columns(author_matrix)
    author_ranks = weightedPageRank(normalized, normalized_weights)
    return showValues(authors, author_ranks)


if __name__ == "__main__":
    inputData = "random_authors.csv"
    weightedAuthorRanks(inputData)
