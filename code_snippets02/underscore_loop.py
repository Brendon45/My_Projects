#!/usr/bin/python3

# Uses of the underscore in Python:

# 1. It is used by the Python interpreter as a variable to store the last value or expression in the interpreter.
# 2. It is used to ignore some values, often in unpacking sequences.
a, _, b = (5, 9, 15)
# The values 5 and 15 have been assigned to 'a' and 'b' respectively, while the value 9 has been ignored using the underscore (_).

# 3. The underscore (_) can also be used as a regular variable.
#    However, by convention, it's often used when the variable will not be used within the loop.
for _ in range(10):
    print(_)

# 4. It is used to separate digits of a number for better readability.
million = 1_000_000
print(million)

