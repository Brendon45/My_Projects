#!/usr/bin/python3

# reversing a given number
def rev_num(num):
    rev = 0
    while num > 0:
         # Extract the last digit of the number
        reminder = num % 10
         # Append the last digit to the reversed number
        rev = (rev * 10) + reminder
        # Remove the last digit from the original number
        num = num // 10
    return rev

# Test the function with a sample number
print(f"reverse of the given number is {rev_num(56789)}")