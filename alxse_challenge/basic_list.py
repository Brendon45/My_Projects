#!/usr/bin/python3

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: Prompt the user to input a middle number and replace the middle number in the list.
mid_number = int(input("Enter the middle number to replace: "))
hat_list[2] = mid_number  # Replace the middle number (index 2) with the user's input.

# Step 2: Remove the last element from the list.
del hat_list[-1]  # Remove the last element from the list.

# Step 3: Print the length of the updated list and the list itself.
print("Length of the updated list:", len(hat_list))
print("Updated list:", hat_list)