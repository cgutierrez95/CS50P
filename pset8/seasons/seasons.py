from datetime import date
import sys, inflect

def main():

    try:
        birth = date.fromisoformat(input('Date of Birth: '))
    except:
        sys.exit('Invalid Date')

    minutes_words = convert(birth)
    print(minutes_words.capitalize(), 'minutes')

def convert(birth):
    p = inflect.engine()

    today = date.today()

    minutes = (today - birth) * 1440

    minutes_words = p.number_to_words(minutes.days, andword="")

    return minutes_words

if __name__ == "__main__":
    main()