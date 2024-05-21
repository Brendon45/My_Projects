#!/usr/bin/python3

def leap_year():
    # Prompt the user to enter the year to be checked
    year = int(input("Enter the year you want to check: "))

    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If divisible by 4, check if it's divisible by 100
        if year % 100 == 0:
            # If divisible by 100, check if it's divisible by 400
            if year % 400 == 0:
                print("This is a leap year")  # If divisible by 400, it's a leap year
            else:
                print("This is not a leap year")  # If not divisible by 400, it's not a leap year
        else:
            print("This is a leap year")  # If not divisible by 100 but divisible by 4, it's a leap year
    else:
        print("This is not a leap year")  # If not divisible by 4, it's not a leap year

# Call the function to check the leap year
leap_year()