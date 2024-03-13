#!/usr/bin/python3

# Printing Brendon's hobby with escaped double quote
print("Brendon's hobby is \"Programming\"", end="\n")

# Informing about playing with operators
print("Now experimenting with operators:")
print()

# Printing results of different arithmetic operations
print("2 to the power of 4 is:", (2**4))
print("2 times 4.0 is:", (2 * 4.))
print("2 times 4 is:", (2 * 4), sep="\n")
print()

# Printing results of floor division for positive and negative numbers
print("2 floored by 4 is:", (2 // 4))
print("-2 floored by 4 is:", (-2 // 4), sep="\n")
print()

# Demonstrating right-associativity of the exponentiation operator
print("3 raised to 2 then raised to answer is:", (2**3**2), sep="\n")

# Assigning string values to variables 'a' and 'b'
a = '1'
b = "1"

# Concatenating and printing the strings stored in variables 'a' and 'b'
print("Concatenating 'a' with 'b' gives:", a + b)
