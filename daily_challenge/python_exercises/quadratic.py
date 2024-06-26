#!/usr/bin/python3

import math

def quadratic_solver():
    """
    Solve a quadratic equation.

    This function takes user input for coefficients (a, b, c) of a quadratic equation
    and calculates the roots based on the discriminant.

    Returns:
        None: The roots are printed.
    """
    try:
        # Input coefficients
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))

        if a == 0:
            print("Coefficient 'a' cannot be zero for a quadratic equation.")
            return

        # Calculate the discriminant
        discriminant = b**2 - 4*a*c

        # Check if the discriminant is positive, negative, or zero
        if discriminant > 0:
            # Two real and distinct roots
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            print(f"Root 1: {root1}")
            print(f"Root 2: {root2}")
        elif discriminant == 0:
            # One real root (repeated)
            root = -b / (2*a)
            print(f"Root: {root}")
        else:
            # Complex roots
            real_part = -b / (2*a)
            imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
            print(f"Root 1: {real_part} + {imaginary_part}i")
            print(f"Root 2: {real_part} - {imaginary_part}i")
    except ValueError:
        print("Invalid input. Please enter numerical values for coefficients.")

# Call the quadratic_solver function
if __name__ == "__main__":
    quadratic_solver()