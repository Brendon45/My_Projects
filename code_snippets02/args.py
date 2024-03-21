#!/usr/bin/env python3

def myfunc(self, *args):
    """
    A function that takes variable number of arguments and prints them.

    Parameters:
    - self: The instance of the class (although not used in this function)
    - *args: Variable number of positional arguments

    Returns:
    - None
    """
    # Print the arguments passed to the function
    print(args)
    
    # Print the number of arguments passed
    print(len(args))
    
    # Print the first argument
    print(args[0])

# Check if the script is run directly
if __name__ == "__main__":
    # Call the myfunc function with arguments 16, 78, 90
    myfunc(16, 78, 90)
