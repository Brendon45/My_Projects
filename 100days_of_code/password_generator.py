#!/usr/bin/python3

import random  # Import the random module for generating random choices

def password_gen():
    # Define the character sets for letters, numbers, and symbols
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '@£%^*&~¬'

    # Greet the user
    print("Welcome to the password generator, making it easier for you!")

    # Prompt the user for the number of letters, numbers, and symbols they want in their password
    noOfLetters = int(input("Enter the number of letters you want to use in your password: "))
    noOfNumbers = int(input("Enter the number of numbers you want to use in your password: "))
    noOfSymbols = int(input("Enter the number of symbols you want to use in your password: "))

    # Create the password list by randomly selecting characters from each category
    list_password = [
        random.choice(letters) for _ in range(noOfLetters)
    ] + [
        random.choice(numbers) for _ in range(noOfNumbers)
    ] + [
        random.choice(symbols) for _ in range(noOfSymbols)
    ]

    # Shuffle the list to ensure a random order of characters
    random.shuffle(list_password)

    # Join the list of characters into a single string
    str_password = ''.join(list_password)

    # Return the generated password
    return str_password

# Ensure the script runs only when executed directly (not when imported as a module)
if __name__ == "__main__":
    # Generate the password by calling the password_gen function
    str_password = password_gen()
    # Print the generated password
    print(f"\nYour password is: {str_password}")