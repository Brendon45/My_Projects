#!/usr/bin/python3

import random
import string

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+{}:\"<>?[];',./\\"
all_chars = lower + upper + numbers + symbols

# Prompt the user to enter the desired length of the password
while True:
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Length must be a positive integer.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer.")

# Prompt the user to enter their desired password
while True:
    password = input("Enter your password: ")
    if len(password) > length:
        print("Password exceeds the specified length. Please enter a password with {} characters or less.".format(length))
    else:
        break

print("Generated Password:", password)
