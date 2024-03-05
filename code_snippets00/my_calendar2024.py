#!/usr/bin/python3

import calendar

yy = 2024

# Loop through each month from January (1) to December (12)
for mm in range(1, 13):
    # Display the calendar for the current month and year
    print(calendar.month(yy, mm))