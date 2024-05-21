#!/usr/bin/python3

# Prompt user to enter their current age
currentAge = input("Enter your current age: ")
currentAge = int(currentAge)

# Calculate remaining time until the age of 90
remainingYears = 90 - currentAge
remainingMonths = remainingYears * 12
remainingWeeks = remainingYears * 52
remainingDays = remainingYears * 365  # Corrected from 356 to 365

# Print the remaining time
print(f"You have {remainingDays} days, {remainingWeeks} weeks, {remainingMonths} months, and {remainingYears} years left")
