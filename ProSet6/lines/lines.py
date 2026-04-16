import sys

def test_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")


def is_hash(text):
    return text.lstrip().startswith("#")
        

def is_blank(text):
    return text.strip() == ""


def main():
    test_arg()
    count = 0
    with open(sys.argv[1]) as f:
        count = sum(1 for line in f if not(is_hash(line) or is_blank(line)))
    print(count)


if __name__ == "__main__":
    main()