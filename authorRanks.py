import csv

import numpy as np

from pageRank import pagerank, showValues


def read_csv_data(csv_file):
    authors_data = []
    with open(csv_file, "r") as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            authors_data.append(row)
    return authors_data


def construct_author_matrix(authors_data):
    unique_authors = list(set([author for row in authors_data for author in row]))
    total_rows = len(unique_authors)
    author_matrix = [[0] * total_rows for _ in range(total_rows)]

    for i, row in enumerate(authors_data):
        for j in range(len(row)):
            for k in range(j + 1, len(row)):
                r = unique_authors.index(row[j])
                c = unique_authors.index(row[k])
                author_matrix[r][c] += 1
                author_matrix[c][r] += 1

    return np.array(author_matrix), unique_authors


def print_author_matrix(author_matrix):
    total_rows = len(author_matrix)
    for i in range(total_rows):
        print(author_matrix[i])


def sum_columns(matrix):
    matrix = np.array(matrix)
    return np.sum(matrix, axis=0)


def author_ranking(author_matrix, column_sum, d=0.85, max_iterations=10):
    n = len(column_sum)
    pr_vector = np.ones(n) / n

    for _ in range(max_iterations):
        new_pr_vector = np.zeros(n)

        for i in range(n):
            for j in range(n):
                if author_matrix[j][i] != 0 and column_sum[j] != 0:
                    new_pr_vector[i] += pr_vector[j] * (
                        1 / sum(1 for x in author_matrix[j] if x != 0)
                    )

        pr_vector = (1 - d) * np.ones(n) / n + d * new_pr_vector

    return pr_vector


def normalize_columns(matrix):
    matrix = np.array(matrix)

    column_sums = sum_columns(matrix)
    non_zero_mask = column_sums != 0
    normalized_matrix = matrix.copy().astype(float)
    normalized_matrix[:, non_zero_mask] /= column_sums[non_zero_mask][np.newaxis, :]

    return normalized_matrix


def original_authorRanks(csv_file: str):
    authors_data = read_csv_data(csv_file)
    author_matrix, authors = construct_author_matrix(authors_data)
    normalized = normalize_columns(author_matrix)
    author_ranks = pagerank(normalized)
    return showValues(authors, author_ranks)


if __name__ == "__main__":
    csv_file = "random_authors.csv"
    original_authorRanks(csv_file)
