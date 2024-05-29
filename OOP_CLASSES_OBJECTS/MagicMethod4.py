#!/usr/bin/python3
'''When we start this program, we can see that it is not possible to
   convert our string x_str, created via str(x), into a Robot object anymore.
'''

# Define the Robot class
class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    # The __repr__ method returns a string that can recreate the object when evaluated
    def __repr__(self):
        return "Robot('" + self.name + "', " + str(self.build_year) + ")"

    # The __str__ method returns a human-readable string representation of the object
    def __str__(self):
        return "Name: " + self.name + ", Build Year: " + str(self.build_year)


if __name__ == "__main__":
    # Create a Robot instance
    x = Robot("marvin", 1979)
    
    # Use the __str__ method to get a string representation of the Robot instance
    x_str = str(x)
    print(x_str)  # Output: Name: marvin, Build Year: 1979
    
    # Print the type of x_str
    print("Type of x_str: ", type(x_str))  # Output: <class 'str'>
    
    # Try to evaluate x_str to create a new Robot instance
    # This will fail because x_str is not a valid expression to recreate the object
    new = eval(x_str)
    print(new)
    print("Type of new:", type(new))