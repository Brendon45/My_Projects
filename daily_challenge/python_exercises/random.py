#!/usr/bin/python3

import random

def generate_random_number():
    """
    Generate a random number within a specified range.

    Prompts the user to input the lower and upper bounds of the range, and then generates
    a random number within that range.
    """
    try:
        # Input lower bound
        lower_bound = int(input("Enter the lower bound: "))
        
        # Input upper bound
        upper_bound = int(input("Enter the upper bound: "))
        
        if lower_bound > upper_bound:
            raise ValueError("Lower bound must be less than or equal to upper bound.")
        
        # Generate random number
        random_number = random.randint(lower_bound, upper_bound)
        print(f"Random number between {lower_bound} and {upper_bound}: {random_number}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate_random_number()
