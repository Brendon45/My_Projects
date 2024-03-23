#!/usr/bin/python3

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Initialize variables for Fibonacci series computation
a, b, series_sum = 0, 1, 0

# Iterate through the Fibonacci series up to the input number
for i in range(number):
    # Print the current Fibonacci number
    print(a, end=', ')
    
    # Calculate the sum of Fibonacci series
    series_sum += a
    
    # Update Fibonacci series variables
    a, b = b, a + b

# Print a newline to separate the series from the sum
print("")

# Print the sum of the Fibonacci series
print(f"The sum is: {series_sum}")
