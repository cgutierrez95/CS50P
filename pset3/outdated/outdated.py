months_text = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December": 12
}

def date():
    while True:

        input_date = input("Date: ")

        if ',' not in input_date and '/' not in input_date:
            continue

        try:
            month, day, year = input_date.split('/')
            if month.isalpha():
                continue
        except:
            month, day, year = input_date.split()

        try:
            day = int(day)
        except:
            day = day.strip(',')

        try:
            day = int(day)
        except:
            continue

        try:
            month = int(month)
        except:
            month = months_text[month]

        if day in months_text or day > 31:
            continue

        if month > 12:
            continue

        print(year.strip(), '-', f"{month:02}", '-',f"{day:02}", sep='')
        return

date()