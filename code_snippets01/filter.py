#!/usr/bin/python3

# Function to check if a number is positive
def is_positive(a):
    return a>0

# Filter positive numbers from the list
output = list(filter(is_positive,[1,-2,3,-4,5,6]))

# Print the filtered output
print(output)