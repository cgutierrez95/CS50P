products = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }



def menu():

    total = 0

    while True:
        try:
            item = input("Item: ")
            item = item.title()
        except EOFError:
            return
        try:
            price = products[item]
            total = total + price
            print('\n''Total:', "${:.2f}".format(total))
        except KeyError:
            pass

menu()