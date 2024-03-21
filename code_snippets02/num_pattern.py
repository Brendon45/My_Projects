#!/usr/bin/env python3

# Shebang line: specifies the Python interpreter to use when executing the script

# Outer loop iterates from 1 to 5
for i in range(1, 6):
    # Inner loop iterates from 1 to i (inclusive)
    for j in range(1, i + 1):
        # Print the value of i without a newline and space as separator
        print(i, end=' ')
    # Move to the next line after printing the values of i for the current iteration
    print('')
