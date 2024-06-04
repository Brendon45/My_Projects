#!/usr/bin/python3
def age_checker():
    try:
        age = int(input("Enter your age: "))

        if 18 <= age <= 45:
            print("Enjoy the ride!")
        elif age < 18:
            print("You're too young for the ride.")
        else:
            print("You're too old for this ride.")
    except ValueError:
        print("Please enter a valid age.")

age_checker()