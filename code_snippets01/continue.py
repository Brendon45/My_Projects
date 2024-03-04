#!/usr/bin/python3

for number in range(1, 6):
# If the number is 3, exit the loop
    if number == 3:
        continue
    # calculate the product of number and 2
    product = number * 2
    # Print out the product in a table form
    print(f"{number} * 2 = {product}")
print('Loop completed')