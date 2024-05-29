#!/usr/bin/python3

# Define a class named Robot
class Robot:
    # The __init__ method initializes the object with name and build_year attributes
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    # The __repr__ method provides a string representation of the Robot object
    # This representation can be used to recreate the object using eval()
    def __repr__(self):
        return "Robot('" + self.name + "', " + str(self.build_year) + ")"

# The following code block runs only if the script is executed directly
if __name__ == "__main__":
    # Create an instance of the Robot class with name "Marvin" and build_year 1979
    x = Robot("Marvin", 1979)
    
    # Convert the Robot instance to its string representation using __repr__
    x_str = str(x)
    print(x_str)  # Output: Robot('Marvin', 1979)
    
    # Print the type of the string representation
    print("Type of x_str: ", type(x_str))  # Output: <class 'str'>
    
    # Use eval to create a new Robot object from the string representation
    new = eval(x_str)
    print(new)  # Output: Robot('Marvin', 1979)
    
    # Print the type of the newly created object
    print("Type of new:", type(new))  # Output: <class '__main__.Robot'>
