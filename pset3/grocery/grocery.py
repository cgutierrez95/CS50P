def grocery():

    list = {}
    tmp = []

    while True:
        try:
            item = input().upper()
        except EOFError:
            for item in list.items():
                tmp.append(item[0])
            tmp.sort()

            for item in tmp:
                print(list[item], item)
            return

        try:
            check = list[item]
            list[item] = list[item] + 1
        except KeyError:
            list[item] = 1

grocery()