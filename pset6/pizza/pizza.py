import sys, csv
from tabulate import tabulate

args = list(sys.argv)
table = []

if len(args) > 2:
    sys.exit('Too many command-line arguments')

if len(args) < 2:
    sys.exit('Too few command-line arguments')

if not args[1].endswith('.csv'):
    sys.exit('Not a CSV file')

try:
    with open(args[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            table.append(row)
        print(tabulate(table, headers="keys",tablefmt="grid"))

except FileNotFoundError:
    sys.exit('File does not exists')