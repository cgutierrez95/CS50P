def main():

    time = input('Time: ').split(":")
    time = int(time[0])
    #convert(time)

    if time >= 7 and time <= 8:
        print('breakfast time')

    if time >= 12 and time <= 13:
        print('lunch time')

    if time >= 18 and time <= 19:
        print('dinner time')


def convert(time):
    ...


if __name__ == "__main__":
    main()