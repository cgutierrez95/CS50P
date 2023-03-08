import csv, sys

args = list(sys.argv)
after = []

if len(args) > 3:
    sys.exit('Too many command-line arguments')

if len(args) < 3:
    sys.exit('Too few command-line arguments')

if not args[1].endswith('.csv') or not args[2].endswith('.csv'):
    sys.exit('Not a CSV file')

try:
    with open(args[1]) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
                last, first = row['name'].split(',')
                house = row['house']
                after.append({"first":first.strip(), "last":last, "house":house})

        with open(args[2], 'w') as output:
                writer = csv.DictWriter(output, fieldnames = ['first', 'last', 'house'])
                writer.writeheader()
                writer.writerows(after)

except FileNotFoundError:
    sys.exit('File does not exists')