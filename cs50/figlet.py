import sys

from pyfiglet import Figlet
import random

figlet = Figlet()

fo = figlet.getFonts()
print(fo)

our_input = input("Type: ")
split_input = our_input.split("-")
try:
    if split_input:
        figlet.setFont(font=split_input[1])
        print(figlet.renderText(our_input))
except Exception:
    figlet.setFont(font=random.choice(fo))
    print(figlet.renderText(our_input))
if not split_input:
    sys.exit(1)
