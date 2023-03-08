amount = 0
print("Amount Due: ", 50)

while 50 > amount:
    coin = input('Insert Coin: ')
    coin = int(coin)

    if coin == 25 or coin == 10 or coin == 5:
        amount = amount + coin

    if amount < 50:
        print("Amount Due: ", 50 - amount)

    if amount >= 50:
        print("Change Owed: ", amount - 50)


