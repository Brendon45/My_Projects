#!/usr/bin/python3
"""We show in the following program that x_repr can still be turned into
   a Robot object"""

# Define the Robot class
class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    # The __repr__ method returns a string representation of the object
    # that can be used to recreate the object with eval
    def __repr__(self):
        return "Robot(\"" + self.name + "\"," + str(self.build_year) + ")"

    # The __str__ method returns a user-friendly string representation
    def __str__(self):
        return "Name: " + self.name + ", Build Year: " + str(self.build_year)


if __name__ == "__main__":
    # Create an instance of the Robot class
    x = Robot("Marvin", 1979)
    
    # Use the repr() function to get the string representation
    # that can recreate the object
    x_repr = repr(x)
    
    # Print the repr string and its type
    print(x_repr, type(x_repr))  # Output: Robot("Marvin",1979) <class 'str'>
    
    # Use eval to create a new Robot object from the repr string
    new = eval(x_repr)
    
    # Print the new Robot object and its type
    print(new)  # Output: Name: Marvin, Build Year: 1979
    print("Type of new:", type(new))  # Output: <class '__main__.Robot'>
