import sys
from pyfiglet import Figlet


def get_font():
    figlet = Figlet()
    return figlet.getFonts()


def main():
    if len(sys.argv) == 1:
        font_text = None
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "-fonts"):
        font_text = sys.argv[2]
    else:
        sys.exit(1)

    if font_text is None:
        import random

        font_text = random.choice(get_font())

    our_input = input("Input: ")
    figlet = Figlet(font=font_text)

    print(figlet.renderText(our_input))


if __name__ == "__main__":
    main()

