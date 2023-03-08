import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    time = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    
    if time:
        time = time.groups()

        initial_hour = int(time[1])
        initial_minute = time[2]
        initial_time = time [3]
        final_hour = int(time[5])
        final_minute = time[6]
        final_time = time [7]

        if (initial_hour > 12 and initial_time == 'PM') or (final_hour > 12 and final_time == 'PM'):
            raise ValueError

        try:
            initial_minute = int(initial_minute)
        except:
            initial_minute = 0

        try:
            final_minute = int(final_minute)
        except:
            final_minute = 0

        if initial_minute > 60 or final_minute > 60:
            raise ValueError

        if initial_time == 'PM' and initial_hour != 12:
            initial_hour += 12

        if initial_time == 'AM' and initial_hour == 12:
            initial_hour = 0

        if final_time == 'PM' and final_hour != 12:
            final_hour += 12
        elif final_time == 'PM' and final_hour == 12:
            final_hour = 12

        new_time = f"{initial_hour:02}" + ':' + f"{initial_minute:02}" + ' to ' + f"{final_hour:02}" + ':' + f"{final_minute:02}"
        return new_time

    else:
        raise ValueError


if __name__ == "__main__":
    main()