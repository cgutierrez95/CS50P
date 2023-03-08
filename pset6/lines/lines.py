import sys

args = list(sys.argv)
counter = 0

if len(args) > 2:
    sys.exit('Too many command-line arguments')

if len(args) < 2:
    sys.exit('Too few command-line arguments')

if not args[1].endswith('.py'):
    sys.exit('Not a Python file')

try:
    with open(args[1]) as file:
        data = file.readlines()
        for line in data:
            if line.startswith('\n'):
                continue
            if line.lstrip().startswith('#'):
                continue
            if line.isspace():
                continue

            counter += 1
    print(counter)

except FileNotFoundError:
    sys.exit('File does not exists')