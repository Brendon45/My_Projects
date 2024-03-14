#!/usr/bin/python3

# Importing the datetime module to get the current year
import datetime

# Ask the user for their date of birth details
year_of_birth = input("Year of birth: ")
month_of_birth = input("Month of birth (1-12): ")
day_of_birth = input("Day of the month: ")

# Get the current year
current_year = datetime.datetime.now().year

# Display the date of birth
print("Your date of birth is:", end=" ")
print(day_of_birth, month_of_birth, year_of_birth, sep="-")

# Calculate the age
age = current_year - int(year_of_birth)

# Display the age
print("You are", age, "years old.")
