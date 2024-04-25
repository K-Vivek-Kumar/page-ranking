import numpy as np

from authorRanks import normalize_columns, read_csv_data
from graphDisplay import create_graph_from_matrix
from pageRank import showValues
from weightRanks import construct_author_matrix, weightedPageRank


def handle_zero_cases(matrix):
    n = matrix.shape[0]
    changes_indices = []
    alone_people = []
    modified_matrix = np.copy(matrix)
    for i in range(n):
        if np.all(matrix[i, :] == 0):
            alone_people.append(i)
            for j in range(n):
                if i != j:
                    modified_matrix[i, j] = 1
            changes_indices.extend([(i, j) for j in range(n) if i != j])
    for j in range(n):
        if np.all(matrix[:, j] == 0):
            for i in range(n):
                if i != j:
                    modified_matrix[i, j] = 1
            changes_indices.extend([(i, j) for i in range(n) if i != j])
    return modified_matrix, changes_indices, alone_people


def removeThem(matrix, authors: list[str], people_to_remove):
    changed = False
    for i in people_to_remove:
        k = authors.index(i[1])
        if matrix[i[0]][k] == 1:
            changed = True
        matrix[i[0]][k] = 0
        matrix[k][i[0]] = 0
    return matrix, changed


def funcs(modified_matrix, author_ranks, alone_people, authors, weights):
    if len(alone_people) == 0:
        return modified_matrix, author_ranks
    node_page_rank_tuples = list(zip(authors, author_ranks))
    sorted_tuples = sorted(node_page_rank_tuples, key=lambda x: x[1], reverse=True)
    changed = False
    for i in alone_people:
        node = authors[i]
        visited = False
        bottom_authors = []
        for val in sorted_tuples:
            if not visited:
                if val[0] == node:
                    visited = True
            else:
                bottom_authors.append((i, val[0]))
        new_modified_matrix, check = removeThem(
            modified_matrix, authors, bottom_authors
        )
        changed = check
    if not changed:
        return modified_matrix, author_ranks
    new_author_ranks = weightedPageRank(normalize_columns(new_modified_matrix), weights)
    return funcs(new_modified_matrix, new_author_ranks, alone_people, authors, weights)


def newIdeaRank(csv_file: str):
    authors_data = read_csv_data(csv_file)
    author_matrix, authors, weights = construct_author_matrix(authors_data)
    create_graph_from_matrix(author_matrix, "pre.png")
    modified_matrix, changed_indices, alone_people = handle_zero_cases(author_matrix)
    create_graph_from_matrix(modified_matrix, "first.png")
    weights = np.array(weights)
    total_weight = np.sum(weights)
    normalized_weights = weights / total_weight
    normalized_matrix = normalize_columns(modified_matrix)
    author_ranks = weightedPageRank(normalized_matrix, normalized_weights)
    new_matrix, new_author_ranks = funcs(
        modified_matrix, author_ranks, alone_people, authors, normalized_weights
    )
    create_graph_from_matrix(new_matrix, "final.png")
    print(new_matrix)
    return showValues(authors, new_author_ranks)


if __name__ == "__main__":
    csv_file = "random_authors.csv"
    newIdeaRank(csv_file)
