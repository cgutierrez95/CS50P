def main():

    greeting = input('Your greeting: ')
    money = value(greeting)
    print(f"${money}")

def value(greeting):


    if 'hello' in greeting.lower().strip():
        return 0

    if 'h' == greeting[0].lower().strip():
        return 20

    return 100


if __name__ == "__main__":
    main()