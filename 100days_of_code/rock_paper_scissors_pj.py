#!/usr/bin/python3

import random  # Import the random module to generate computer's move

def computers_choice():
    """
    Function to generate the computer's move.
    Returns the computer's choice.
    """
    computer_choice = random.randrange(0, 3)
    print("Choices:\n0 for Rock\n1 for Paper\n2 for Scissors\n")
    print(f"Computer's choice is: {computer_choice}.")
    return invalid_user_choice(computer_choice)

def invalid_user_choice(computer_choice):
    """
    Function to handle invalid user input.
    Prompts user until a valid input (0, 1, or 2) is entered.
    """
    try:
        user_choice = int(input("User's choice (0, 1, 2): "))
        if user_choice < 0 or user_choice > 2:
            print("\nInvalid input. Enter choice again!\n")
            return invalid_user_choice(computer_choice)
        else:
            return valid_user_choice(user_choice, computer_choice)
    except ValueError:
        print("\nInvalid input. Please enter a number (0, 1, or 2).\n")
        return invalid_user_choice(computer_choice)

def valid_user_choice(user_choice, computer_choice):
    """
    Function to compare user and computer choices and determine the winner.
    """
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("User wins!")
    else:
        print("Computer wins!")

# Execute the game by calling the function
computers_choice()