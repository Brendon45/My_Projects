#!/usr/bin/python3
"""The topic of this subsection will be the special methods __getattr__ and
 __setattr__, but before we talk about them we need some incentive. Let's look
 at the following Python class:
"""

# Initial Robot class with property decorators
class Robot:
    def __init__(self, name, build_year, city):
        self.name = name
        self.build_year = build_year
        self.city = city

    @property
    def name(self):
        return self.__name

    @property
    def build_year(self):
        return self.__build_year

    @property
    def city(self):
        return self.__city

    @name.setter
    def name(self, value):
        self.__name = value

    @build_year.setter
    def build_year(self, value):
        self.__build_year = value

    @city.setter
    def city(self, value):
        self.__city = value


# Example usage of the initial Robot class
robot = Robot("RoboBot", 2022, "TechCity")
print("> Before:\n________")
print(robot.name)
print(robot.build_year)
print(robot.city)

"""
We observe that the process of creating getters and setters involves repetitive patterns.
It would be advantageous to employ generic getters and setters,
as demonstrated in the following example. In this example, we use the
__getattr__ and __setattr__ special methods to manage attributes.
These methods are invoked automatically when attribute access or assignment occurs on an object.
"""

# Improved Robot class with __getattr__ and __setattr__
class Robot:
    def __init__(self, name, build_year, city):
        self.name = name
        self.build_year = build_year
        self.city = city

    # __getattr__ is called when an attribute is not found in the usual places
    def __getattr__(self, name):
        return self.__dict__[f"__{name}"]

    # __setattr__ is called when an attribute assignment is attempted
    def __setattr__(self, name, value):
        self.__dict__[f"__{name}"] = value


# Example usage of the improved Robot class
robot = Robot("RoboBot", 2022, "TechCity")
print()
print("> After:\n________")
print(robot.name)
print(robot.build_year)
print(robot.city)

"""
Now, what happens if certain attributes have some conditions to fulfill?
No problem, we can just add them to the __setattr__ method, like in the following example:
"""

# Further improved Robot class with validation in __setattr__
class Robot:
    def __init__(self, name, build_year, city):
        self.name = name
        self.build_year = build_year
        self.city = city

    # __getattr__ to access attributes with a prefix
    def __getattr__(self, name):
        return self.__dict__[f"__{name}"]

    # __setattr__ with validation for certain attributes
    def __setattr__(self, name, value):
        if name == 'name':
            if value in ['Henry', 'Oscar']:
                raise ValueError('Not a decent Robot name')
        elif name == 'build_year':
            if int(value) < 2020:
                raise ValueError('Build year has to be after 2019')
        self.__dict__[f"__{name}"] = value


# Example usage of the validated Robot class
robot = Robot("Marvin", 2020, "TechCity")
print()
print(">> Now:\n________")
print(robot.name)
print(robot.build_year)
print(robot.city)

# Trying to create a robot with an invalid name or build year will raise an error
# robot_invalid = Robot("Henry", 2020, "TechCity")  # ValueError: Not a decent Robot name
# robot_invalid_year = Robot("Marvin", 2019, "TechCity")  # ValueError: Build year has to be after 2019
