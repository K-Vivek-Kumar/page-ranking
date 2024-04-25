import csv

file_path = "goverment.txt"
with open(file_path, "r") as file:
    data_txt = file.readlines()

rows = [line.strip().split("\t") for line in data_txt]

csv_file_path = "data.csv"
with open(csv_file_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)

print(f"Data saved to {csv_file_path}")
