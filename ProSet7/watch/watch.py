import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"<iframe (?:.*)?src=\"https?://(?:www\.)?youtube\.com/embed/(.+?)\">", s, re.IGNORECASE):
        suffix = matches.group(1)
        new_url = f"https://youtu.be/{suffix}"
        return new_url
    return None


if __name__ == "__main__":
    main()