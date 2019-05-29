"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
AUTHOR: RAISS BAHATI
--------------------------------
"""

import random

def start_game():

    print("WELCOME TO THE NUMBER GUESSING GAME")
    secret_number = random.randint(1, 20)
    number_of_tries = 0

    while True:
    	try:
    	
        	user_guess = int(input("Please enter a number between 1-20: "))
        except ValueError as err:
        	print("Please enter a number: {}".format(err))
        number_of_tries += 1

        if user_guess < secret_number:
            print("It's lower")

        elif user_guess > secret_number:
            print("It's higher")

        else:
            break

    print("You got it!")
    print("You guessed the number after {} tries!".format(number_of_tries))
    print("Thank you for playing and see you soon")


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
