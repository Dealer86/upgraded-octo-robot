# Guessing Game
# I’m thinking of a number between 1 and 100…
#
# What is it?
# In a file called game.py, implement a program that:
#
# Prompts the user for a level,
# . If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and n
# , inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.


import random


def get_level():
    while True:
        level = input("Level: ")
        if not level.isdigit():
            continue
        if int(level) <= 0:
            continue
        else:
            return int(level)


def generate_number_between_1_n(n: int):
    return random.randint(1, n)


def guess_number():
    while True:
        guess = input("Guess: ")
        if not guess.isdigit():
            continue
        if int(guess) <= 0:
            continue

        else:
            if int(guess) < level:
                print("Too small!")
                continue
            elif int(guess) > level:
                print("Too big!")
                continue
            else:
                print("Just right!")
                break


level = generate_number_between_1_n(get_level())

guess_number()
