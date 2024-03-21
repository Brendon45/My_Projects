#!/usr/bin/env python3

## Program to find the maximum number in a list of numbers

# Prompt the user to enter the number of numbers they want
number = int(input("Enter the number of numbers you want: "))

# Initialize an empty list to store the numbers
number_list = []

# Iterate through the range of numbers specified by the user
for i in range(number):
    # Prompt the user to enter each number and append it to the list
    number_list.append(int(input(f"Enter number {i + 1}: ")))

# Initialize a variable 'max' with the second element of the list
max = number_list[0]

# Iterate through each number in the list
for i in number_list:
    # Check if the current number is greater than 'max'
    if i > max:
        # If it is, update 'max' to the current number
        max = i

# Print the list of numbers entered by the user
print(f"Your list: {number_list}")

# Print the maximum number found in the list
print(f"Max number is: {max}")
