import inflect

def adieu():

    p = inflect.engine()
    name_list = []

    while True:

        try:
            name = input("Name: ")
            name_list.append(name)
        except EOFError:
            list = p.join((name_list))
            print('Adieu, adieu, to',list)
            return




adieu()