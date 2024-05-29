#!/usr/bin/python3

# Define a class A
class A:
    # Define the __str__ method to return the string "42"
    def __str__(self):
        return "42"

# Create an instance of class A
a = A()

# Print the result of the repr() function applied to the instance a
# By default, if __repr__ is not defined, it uses the __repr__ method from the base class,
# which provides a string with the object's class name and memory address.
print(repr(a))

# Print the result of the str() function applied to the instance a
# This calls the __str__ method of the instance a, which returns the string "42".
print(str(a))
