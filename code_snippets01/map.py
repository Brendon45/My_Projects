#!/usr/bin/python3

def add_list(a,b):
    """Function to add two lists element-wise."""

    return a+b
# Apply the add_list function to each pair of elements from the two lists using map
output = list(map(add_list,[2,6,3],[3,4,5]))
print(output)