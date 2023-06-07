from pyfiglet import Figlet
import random
import sys

figlet = Figlet()


def main():
    font_choice = choice()
    txt = input("Input: ")
    figlet.setFont(font=font_choice)
    print(figlet.renderText(txt))


def choice():
    if len(sys.argv) == 1:
        return random.choice(figlet.getFonts())
    elif (
        len(sys.argv) == 3
        and sys.argv[1] == "-f"
        or sys.argv[1] == "--font"
        and sys.argv[1] in figlet.getFonts()
    ):
        return sys.argv[2]
    else:
        return sys.exit("Invalid usage")


main()
