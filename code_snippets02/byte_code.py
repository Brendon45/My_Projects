#!/usr/bin/env python3

from dis import dis

# Define a function 'my_func' that takes an argument 'n'
def my_func(n):
    # Check if 'n' is greater than 5
    if n > 5:
        return n  # Return 'n' if it's greater than 5
    else:
        return n + 5  # Return 'n + 5' if 'n' is less than or equal to 5

# Display the disassembled bytecode of the 'my_func' function
print(dis(my_func))
