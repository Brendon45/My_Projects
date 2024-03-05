#!/usr/bin/python3

# Pythonic iteration using enumerator and zip
names = ["Ashley", "Brandon", "Charlie"]
ages = [25, 36, 22]

# Enumerate for index and value
for index, name in enumerate(names):
    print(f"Person {index + 1}: {name}")

# Zip for parallel iteration
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
