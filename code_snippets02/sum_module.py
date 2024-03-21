#!/usr/bin/env python3

# Shebang line: specifies the Python interpreter to use when executing the script

# Print a message indicating that the module was imported successfully
print("Module imported successfully")

# Define a function to add the numbers in a list
def add_list_numbers(my_list):
    """
    Add the numbers in the given list.

    Parameters:
    - my_list: The list of numbers.

    Returns:
    - The sum of the numbers in the list.
    """
    # Initialize the sum
    sum = 0
    # Iterate through the list
    for i in my_list:
        # Add each number to the sum
        sum += i
    # Return the sum
    return sum
