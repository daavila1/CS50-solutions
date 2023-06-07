import random
import sys


def main():
    number = rand_int()
    game(number)


def rand_int():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                raise ValueError

        except ValueError:
            pass

        else:
            return random.randint(1, level)


def game(number):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                raise ValueError

        except ValueError:
            pass

        else:
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                sys.exit("Just right!")

main()
