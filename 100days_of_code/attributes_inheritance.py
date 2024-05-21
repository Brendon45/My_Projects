#!/usr/bin/python3

import os  # Import the os module to clear the screen

def add_to_dict(data_dict):
    """
    Function to add a new bid to the data dictionary.
    Prompts the user for their name and bid amount.
    """
    name = input("Enter your name: ")
    bid = int(input("What's your bid: "))
    data_dict[name] = bid

    # Clear the screen after adding a bid
    clear_screen()

def clear_screen():
    """
    Function to clear the console screen.
    Works for both Windows and Unix-like systems.
    """
    if os.name == 'nt':
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Unix/Linux/Mac

# Dictionary to store user data (name and bid amount)
user_data = {}

# Add the first bid
add_to_dict(user_data)

# Loop to add additional bids
while True:
    choice = input("Is anyone else ready to bid? (yes or no): ").strip().lower()
    if choice == 'yes' or choice == 'y':
        add_to_dict(user_data)
    elif choice == 'no' or choice == 'n':
        break  # Exit the loop if no more bids are to be added
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Determine and print the highest bidder
if user_data:
    highest_bidder = max(user_data, key=user_data.get)
    max_value = user_data[highest_bidder]
    print(f"The highest bidder is {highest_bidder} with a bid of {max_value}.")
else:
    print("No one placed a bid today.")