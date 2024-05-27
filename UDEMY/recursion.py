# Tutorial 41-Python Recursion

# Define a recursive function to calculate the factorial of a number
def fact(n):
    # Base case: if n is 1 or less, the factorial is 1
    if n <= 1:
        return 1
    # Recursive case: n multiplied by the factorial of (n-1)
    return n * fact(n-1)
# Print the factorial of 5 using the recursive function
print("Factorial of 5 is", fact(5))