#!/usr/bin/python3


def greeting(first_name, last_name, title, middle_name=None):
    if middle_name is not None:
        str_to_return = f"Hi {title}, your full name is {first_name} {middle_name} {last_name}"
    else:
        str_to_return = f"Hi {title}, your full name is {first_name} {last_name}"
    return str_to_return

brendon = greeting("Brendon", "Jeje", "Mr")
print(brendon)