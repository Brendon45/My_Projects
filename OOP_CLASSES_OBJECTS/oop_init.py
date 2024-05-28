#!/usr/bin/python3
# This is a simple Python class program

# Define a class named 'Person'
class Person:
    # Define the initializer method with a parameter 'name'
    def __init__(self, name):
        self.name = name  # Initialize the instance variable 'name' with the value passed

    # Define a method 'say_hi' to print a greeting message
    def say_hi(self):
        # Print a greeting message that includes the person's name
        print('Hello, my name is', self.name)

# Create an instance of the 'Person' class with the name 'John Smith'
p = Person('John Smith')
# Call the 'say_hi' method on the 'Person' instance to print the greeting
p.say_hi()
