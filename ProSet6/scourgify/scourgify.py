import csv
import sys

def test_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


def main():
    test_arg()
    try:
        with open(sys.argv[1]) as before,\
             open(sys.argv[2], "w", newline="") as after: #if newline
                reader = csv.DictReader(before)
                writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for line in reader:
                    last, first = line["name"].strip('"').split(", ")
                    house = line["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()