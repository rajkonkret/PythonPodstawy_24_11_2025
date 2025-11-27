import csv

# filename = "records.csv"
filename = "records_discount.csv"

fields = []
rows = []

with open(filename, "r") as csv_f:
    # wczytanie fragmentu pliku w celu wyszukania znaku podziału
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter)  # ;
    print(dialect.quotechar)  # "

    csv_f.seek(0)  # ustawienie odczytu na początek pliku
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)
    # csvreader = csv.reader(csv_f, delimiter=";")
    print(csvreader)
    # <_csv.reader object at 0x0000016B018041C0> - iterator

    fields = next(csvreader)  # odczyt pierwszego wiersza danych

    for row in csvreader:  # zaczyna od drugiego wiersza
        rows.append(row)

print('Fields:', fields)
print("Rows:", rows)
# Fields: ['name', 'branch', 'year', 'cgpa']
# Rows: [['radek', 'coe', '3', '0']]

# Fields: ['sku;exp_date;price']
# Rows: [['1;today;200'], ['2;today;100'], ['3;tomorrow;50'], ['4;today;49.99'], ['5;today;100']]
# Fields: ['sku', 'exp_date', 'price']
# Rows: [['1', 'today', '200'],
# ['2', 'today', '100'],
# ['3', 'tomorrow', '50'],
# ['4', 'today', '49.99'],
# ['5', 'today', '100']]