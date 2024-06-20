#!/usr/bin/python3

import calendar

def display_calendar():
    """
    Display the calendar for a given month and year.
    
    Prompts the user to input a year and a month, and then prints the corresponding calendar.
    """
    try:
        # Input year with validation
        year = int(input("Enter year (e.g., 2024): "))
        if year < 1:
            raise ValueError("Year must be a positive integer.")
        
        # Input month with validation
        month = int(input("Enter month (1-12): "))
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12.")
        
        # Display the calendar
        cal = calendar.month(year, month)
        print(cal)
    except ValueError as e:
        print(f"Invalid input: {e}")
        print("Please enter a valid year and month.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    display_calendar()