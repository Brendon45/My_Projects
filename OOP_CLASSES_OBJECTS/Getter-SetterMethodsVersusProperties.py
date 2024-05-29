#!/usr/bin/python3
"""Determining the Right Path: Getter-Setter Methods Versus Properties in Python

The recommended and Pythonic approach is to use properties. Is this always the
case, or are there situations where employing getter and setter methods is the
preferable choice? We will show some use cases where getters and setters might
be the better choice.

1. Dynamic Computation or Validation: If getting or setting an attribute involves
complex computations or validation that goes beyond simple attribute access,
using getter and setter methods allows you to encapsulate this logic more
explicitly.
"""

# Example 1: Dynamic Computation or Validation
class Circle:
    def __init__(self, radius):
        self._radius = radius

    # Getter method to compute the area dynamically
    def get_area(self):
        return 3.14 * self._radius ** 2

    # Setter method with validation
    def set_radius(self, value):
        if value < 0:
            raise ValueError("Radius must be non-negative")
        self._radius = value

# Example usage
circle = Circle(7)
print(f'THE AREA OF CIRCLE = {circle.get_area()} m^2')
print()

"""
2. External API Compatibility: When working with external APIs or libraries
that expect traditional getter and setter methods, adhering to their conventions
may be necessary for compatibility. You may have a popular Java implementation
of a class and you write a Python class which has to simulate the interface
for example.

3. Additional Arguments to Attributes: Let's consider an example with a Person
class which has an attribute height, and the setter method (set_height) includes
additional logic to ensure that the height is within a valid range. The additional
argument (validate) controls whether the validation should be performed:
"""

# Example 3: Additional Arguments to Attributes
class Person:
    def __init__(self, name, height):
        self.name = name
        self._height = height

    # Getter method for height
    def get_height(self):
        return self._height

    # Setter method for height with optional validation
    def set_height(self, value, validate=True):
        if validate and not (150 <= value <= 200):
            raise ValueError("Height must be between 150 and 200 cm.")
        self._height = value

# Example usage
person = Person("Alice", height=170)

# Try setting height within the valid range
person.set_height(175)
print(person.get_height())

# Try setting height outside the valid range
try:
    person.set_height(210)
except ValueError as e:
    print(e)

# Set height outside the valid range with validation disabled
person.set_height(210, validate=False)
print(person.get_height())

"""
We can see that if we set validate to False, we can set height values outside of the valid range!
"""
