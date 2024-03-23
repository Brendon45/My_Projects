#!/usr/bin/python3

# Initialize a list containing numbers from 1 to 24 using the range function
my_list = list(range(1, 25))

# Initialize empty lists to store even and odd numbers
even_numbers = []
odd_numbers = []

# Iterate through each number in my_list
for number in my_list:
    # Check if the number is even (divisible by 2 with no remainder)
    if number % 2 == 0:
        # Append even numbers to the even_numbers list
        even_numbers.append(number)
    else:
        # Append odd numbers to the odd_numbers list
        odd_numbers.append(number)

# Print the list of even numbers
print("List of even numbers:", even_numbers)

# Print the list of odd numbers
print("List of odd numbers:", odd_numbers)
