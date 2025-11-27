import csv

filename = "records.csv"

fields = []
rows = []

with open(filename, "r") as csv_f:
    csvreader = csv.reader(csv_f)
    print(csvreader)
    # <_csv.reader object at 0x0000016B018041C0> - iterator

    fields = next(csvreader)  # odczyt pierwszego wiersza danych

    for row in csvreader:  # zaczyna od drugiego wiersza
        rows.append(row)

print('Fields:', fields)
print("Rows:", rows)
# Fields: ['name', 'branch', 'year', 'cgpa']
# Rows: [['radek', 'coe', '3', '0']]