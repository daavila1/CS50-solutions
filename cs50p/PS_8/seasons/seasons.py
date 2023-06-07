import inflect
import datetime
import sys
import re

p = inflect.engine()


def main():
    try:
        inpt = input("Date of birth: ")
        birthday, today = get_dates(inpt)

    except ValueError:
        sys.exit("Invalid date")

    else:
        # print(type({birthday}))
        # print(type({today}))
        minutes = get_diff(birthday, today)
        words = p.number_to_words(minutes, andword="").capitalize()
        print(words, "minutes")


def get_dates(birth):
    # birth = input("Date of birth: ")
    if _ := re.search(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$", birth):
        year, month, day = birth.split("-")
        birth = datetime.date(int(year), int(month), int(day))
        today = datetime.date.today()
        return birth, today

    else:
        raise ValueError


def get_diff(birthday, today):
    diff = today - birthday
    # print(type({diff}))
    return diff.days * 24 * 60


if __name__ == "__main__":
    main()
