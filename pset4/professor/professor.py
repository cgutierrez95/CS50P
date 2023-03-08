import random


def main():
    score = 0
    level = get_level()

    for i in range(10):
        x,y = generate_integer(level)
        msg = str(x) + " + " + str(y) + " = "
        try:
            result = int(input(msg))
        except:
            result = "a"

        for j in range(3):
            if result == (x+y):
                score = score + 1
                break
            elif j == 2:
                print("EEE")
                print(msg, x+y)
            else:
                print("EEE")
                try:
                    result = int(input(msg))
                except:
                    result = "a"

    print("Score: ", score)

def get_level():

    level = 0

    while level < 1 or level > 3:
        try:
            level = int(input("Level: "))
        except:
            continue

    return level


def generate_integer(level):
    if level == 1:

        x = random.randint(0, 9)
        y = random.randint(0, 9)

        return x ,y

    if level == 2:

        x = random.randint(10, 99)
        y = random.randint(10, 99)

        return x ,y

    if level == 3:

        x = random.randint(100, 999)
        y = random.randint(100, 999)

        return x ,y

if __name__ == "__main__":
    main()