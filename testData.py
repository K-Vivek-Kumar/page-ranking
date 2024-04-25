import csv
import random


def generate_random_csv(
    authors_list,
    min_authors_per_row,
    max_authors_per_row,
    total_rows,
    output_file,
    special_people,
    special_rows_count,
):
    # Assign weights to authors based on a custom distribution (e.g., inversely proportional to index)
    weights = [
        1 / (i + 1) for i in range(len(authors_list))
    ]  # Example: Inverse proportional to index

    # Set up special people who will appear in rows with all "1" values
    special_people_set = set(special_people)

    with open(output_file, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)

        for _ in range(total_rows):
            num_authors = random.randint(min_authors_per_row, max_authors_per_row)

            row_authors = random.choices(authors_list, weights=weights, k=num_authors)

            if special_people_set and random.random() < special_rows_count / total_rows:
                row_authors = random.choices(list(special_people_set), k=1)
                num_authors = len(row_authors)

            csv_writer.writerow(row_authors)

    print(f"Random CSV data generated successfully in '{output_file}'.")


authors_list = [f"A{x}" for x in range(200)]

min_authors_per_row = 1
max_authors_per_row = 7
total_rows = 10000
output_file = "random_authors.csv"

# Specify special people to include in rows with all "1" values
special_people = ["AVivek", "AAdarsh", "ASai", "AToday", "ATomorrow"]
special_rows_count = 6

generate_random_csv(
    authors_list,
    min_authors_per_row,
    max_authors_per_row,
    total_rows,
    output_file,
    special_people,
    special_rows_count,
)
