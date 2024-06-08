import random

def get_computer_choice():
    """Randomly returns 'rock', 'paper' or 'scissors'"""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    """Gets user input and requests it"""
    user_input = input("Enter rock, paper, or scissors (or 'q' to quit): ").lower()
    while user_input not in ["rock", "paper", "scissors", 'q']:
        user_input = input("Invalid choice. Enter rock, paper, or scissors: ")
    return user_input

def determine_winner(user_choice, computer_choice):
    """Determines and returns the winner"""
    if  user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"
    
def play_game():
    """Plays rounds of Rock, Paper, Scissors until the user decides to quit"""
    while True:
        user_choice = get_user_choice
        if user_choice == 'q':
            break
        computer_choice = get_computer_choice
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

play_game()
