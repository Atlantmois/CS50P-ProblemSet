from pyfiglet import Figlet
from pyfiglet import FontNotFound
import random
import sys

figlet = Figlet()

if len(sys.argv) == 1:
    fonts = figlet.getFonts()
    randomFont = random.choice(fonts)
    figlet.setFont(font=randomFont)
    text = input("Input: ")
    print(f"Output: {figlet.renderText(text)}")
elif len(sys.argv) == 3 and sys.argv[1] == "-f":
    try:
        figlet.setFont(font=sys.argv[2])
    except FontNotFound:
        sys.exit("Invalid usage")
    text = input("Input: ")
    print(f"Output: {figlet.renderText(text)}")
else:
    sys.exit("Invalid usage")
