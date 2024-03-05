#!/usr/bin/python3

# Outer loop iterating from 1 to 8
for i in range(1, 9):
    # Inner loop iterating from 9 to i (exclusive) in descending order
    # The step size is -1, meaning it decrements by 1 in each iteration
    for j in range(9, i, -1):
        # Printing the value of i without a newline
        print(i, end="")
    # Printing a newline after each inner loop iteration
    print()