def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):

    if len(plate) > 6 or len(plate) < 2:
        return False

    if plate[0:1].isdigit():
        return False

    for letter in plate:
        if not letter.isalnum():
            return False

    for i, letter in enumerate(plate):
        if letter.isdigit():

            if letter == '0':
                return False

            if not plate[i:].isdigit():
                return False
            break

    return True
main()