#!/usr/bin/python3

# Prompt the user to enter a number
num = input("Enter a number: ")

# Convert the input string to an integer
num = int(num)

# Check if the number is 0
if num == 0:
    print("You entered 0")
# Check if the number is even
elif num % 2 == 0:
    print("Your number is even")
# If the number is not 0 and not even, it must be odd
else:
    print("Your number is odd")