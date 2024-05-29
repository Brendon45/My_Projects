#!/usr/bin/python3

# Define a class A
class A:
    # Define the __repr__ method to return the string "42"
    def __repr__(self):
        return "42"

# Create an instance of class A
a = A()

# Print the result of the repr() function applied to the instance a
# This calls the __repr__ method of the instance a, which returns the string "42".
print(repr(a))  # Output: 42

# Print the result of the str() function applied to the instance a
# Since class A does not define a __str__ method, it falls back to using the __repr__ method.
print(str(a))  # Output: 42

# Output the object directly
# This will implicitly call the __repr__ method and output the result.
a  # Output: 42 (in an interactive interpreter or script)
