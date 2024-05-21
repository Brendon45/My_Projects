#!/usr/bin/python3

# Prompt user to enter the values of a and b
a = input("Enter value of a: ")
b = input("Enter value of b: ")

# Swapping values using a temporary variable
temp = a  # A temporary container to hold value of a
a = b  # Assigning value of b to a
b = temp  # Assigning the value of a which was stored in temp to b

# Printing the values after swapping
print(f"a = {a}")
print(f"b = {b}")
