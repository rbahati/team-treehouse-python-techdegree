"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
AUTHOR: RAISS BAHATI
--------------------------------
"""

import random

def start_game():

    print("WELCOME TO THE NUMBER GUESSING GAME!")
    secret_number = random.randint(1, 20)
    number_of_tries = 0
    scores = []
    play = True

    while play:
        
        try:
            user_guess = int(input("Please enter a number between 1-20: "))
            
            if user_guess > 20:
                raise ValueError("The number you entered is above the range between 1-20")
                number_of_tries += 1
            elif user_guess < 1 :
                raise ValueError("The number you entered is below the range between 1-20")
                number_of_tries += 1
        except ValueError as err:
            print("Please try again!", "Here is the specific error message => {}".format(err))
            number_of_tries += 1
        else:
            number_of_tries += 1

            if user_guess < secret_number:
                print("It's lower")

            elif user_guess > secret_number:
                print("It's higher")

            else:
                print("You got it!")
                print("You guessed the number after {} tries!".format(number_of_tries))
                scores.append(number_of_tries)
                play_again = input("Would you like to play again(Y/N)? ")
                if play_again.lower().startswith("y"):
                    number_of_tries = 0
                    secret_number = random.randint(1, 20)
                    print("The score to beat is {}".format(min(scores)))
                    continue
                elif play_again.lower().startswith("n"):
                    print("Thank you for playing and see you soon")
                    play = False

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
