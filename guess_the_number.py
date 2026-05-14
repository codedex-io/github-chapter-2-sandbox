
import random


def main():
    level = Level_setting()
    Guess_number(level)
    return


#  STEP 1:  Prompts the user for a level, 𝑛.
#           If the user does not input a positive integer, the program should prompt again.
def Level_setting():
    while True:
        try:
            Level = input("Level: ")
            # The Guess should not be negative or string
            if Level == Level.isalpha():
                raise ValueError

            Level = int(Level)

            if Level <= 0:
                continue
            else:
                return Level

        except ValueError:
            continue

    # STEP 2: Randomly generates an integer between 1 and 𝑛


def Guess_number(level):
    number = random.randint(1, level)
    while True:
        try:
            Guess = input("Guess: ")
            # the Guess should not be negative or string
            if Guess.isalpha():
                raise ValueError

            Guess = int(Guess)

            if Guess <= 0:
                continue
                # STEP 3: check if the number is == Guess
            elif Guess < number:
                print("Too small!")
                continue

            elif Guess > number:
                print("Too large!")
                continue

            elif Guess == number:
                print("Just right!")
                return

        except ValueError:
            continue


main()
