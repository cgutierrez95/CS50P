def gauge():

    fuel = input("Fraction: ")
    try:
        x,y = fuel.split('/')
    except ValueError:
        return 1

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return 1

    if y == 0:
        return 1

    if x > y:
        return 1

    fuel_level = (x / y)

    if fuel_level <= .01:
        print('E')
        return 0

    if fuel_level >= .99:
        print('F')
        return 0

    fuel_level = "{:.0%}".format(fuel_level)
    print(fuel_level)
    return 0

status = 1
while status >= 1:
    status = gauge()
