import random


def game():

    level = 0
    guess = 0

    while level <= 0 :
        try:
            level = int(input("Level: "))
        except:
            continue

    number = random.randint(1, level)

    while number != guess:

        try:
            guess = int(input("Guess: "))
        except:
            continue

        if number == guess:
            print("Just right!")
            return

        if number < guess:
            print("Too large!")

        if number > guess:
            print("Too small!")

game()