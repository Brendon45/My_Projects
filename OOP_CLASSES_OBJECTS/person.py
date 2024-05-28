#!/usr/bin/python3

# Define a class named 'Person'
class Person:
    def __init__(self, name, age):
        # Initialize the 'name' and 'age' attributes
        self.name = name
        self.age = age

    def __str__(self):
        # Define the string representation of the object for end users
        return f"I'm {self.name}, and I'm {self.age} years old."

    def __repr__(self):
        # Define the official string representation of the object, useful for debugging
        return f"{type(self).__name__}(name='{self.name}', age={self.age})"

# Example usage:
p = Person('Tinashe Mureza', 30)
print(str(p))  # Output: I'm Tinashe Mureza, and I'm 30 years old.
print(repr(p))  # Output: Person(name='Tinashe Mureza', age=30)