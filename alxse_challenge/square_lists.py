#!/usr/bin/python3
"""Generate the squares of the members of a given list"""
nums = [1, 2, 3, 4]

for_nums = []
# use a for loop
for num in nums:
    for_nums.append(num ** 2)

print(f"Before: {nums}")
print(f"After for loop: {for_nums}")
print()
# use list comprehension
compr_nums = [num ** 2 for num in nums]
print(f"After list comprehension: {compr_nums}")