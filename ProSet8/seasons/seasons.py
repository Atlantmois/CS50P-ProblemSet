from datetime import date
import sys

import inflect


def main():
    try:
        birth_date = date.fromisoformat(input("Date of Birth: ").strip())
    except ValueError:
        sys.exit("Invalid date")
    today = date.today()
    print(f"{convert(get_diff(birth_date, today))} minutes")


def get_diff(birth_date, today):
    return (today - birth_date).days * 24 * 60


def convert(minutes):
    p = inflect.engine()
    return p.number_to_words(minutes, andword="").capitalize() # type: ignore (pylance bug)


if __name__ == "__main__":
    main()
