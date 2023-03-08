def main():

    fraction = input("Fraction: ")
    fuel_level = convert(fraction)
    fuel_level = gauge(fuel_level)
    print(fuel_level)

def convert(fraction):

    try:
        x,y = fraction.split('/')
    except ValueError:
        return 1

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return 1

    if y == 0:
        raise ZeroDivisionError

    if x > y:
        raise ValueError

    fuel_level = (x / y) * 100
    return fuel_level


def gauge(percentage):

    if percentage <= 1:
        return 'E'

    if percentage >= 99:
        return 'F'

    percentage = percentage / 100

    percentage = "{:.0%}".format(percentage)
    return percentage

if __name__ == "__main__":
    main()