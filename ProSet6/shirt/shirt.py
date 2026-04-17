import sys
from os import path

from PIL import Image, ImageOps


def test_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    ext1, ext2 = path.splitext(sys.argv[1])[1], path.splitext(sys.argv[2])[1]
    ext_tuple = (".jpg", ".jpeg", ".png")
    if ext1 not in ext_tuple:
        sys.exit("Invalid input")
    elif ext2 not in ext_tuple:
        sys.exit("Invalid output")
    elif ext1 != ext2:
        sys.exit("Input and output have different extensions")


def main():
    test_arg()
    try:
        shirt = Image.open("shirt.png")
        size = shirt.size
        photo = Image.open(sys.argv[1])
        photo = ImageOps.fit(image=photo, size=size)
        photo.paste(shirt, shirt)
        photo.save(fp=sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
