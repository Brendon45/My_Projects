#!/usr/bin/env python3

# Shebang line: specifies the Python interpreter to use when executing the script

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Outer loop iterates from 1 to the entered number (inclusive)
for row in range(1, number + 1):
    # Inner loop iterates from 1 to the current row number (inclusive)
    for column in range(1, row + 1):
        # Print the product of the current row and column numbers without a newline and space as separator
        print(row * column, end=' ')
    # Move to the next line after printing all values for the current row
    print()
