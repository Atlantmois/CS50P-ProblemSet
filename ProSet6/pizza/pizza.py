import csv
import sys
from tabulate import tabulate

def test_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif  not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


def main():
    test_arg()
    try:
        with open(sys.argv[1]) as f:
            f = csv.reader(f)
            headers = next(f)   
            tab = [row for row in f]
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(tabulate(tab, headers, tablefmt="grid"))


if __name__ == "__main__":
    main()