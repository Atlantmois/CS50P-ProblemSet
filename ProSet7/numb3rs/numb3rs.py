import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})"
    if not (matches := re.fullmatch(pattern, ip)):
        return False
    for i in range(1, 5):
        if not str(int(matches.group(i))) == matches.group(i):
            return False
        if not 0 <= int(matches.group(i)) <= 255:
            return False
    return True


if __name__ == "__main__":
    main()