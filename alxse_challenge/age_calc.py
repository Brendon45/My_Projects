#!/usr/bin/python3
# Age calculator 
yob = input("What's your year of birth: ")
mob = input("Month of birth (0 - 12): ")
dob = input("Day of the month: ")
current_year = input("In which year are you now? ")

# calculate the age 
age = int(current_year) - int(yob)

print("Your date of birth is ", end=" ")
print(dob,"-",mob,"-",yob)

# display the age
print("You are", age, end=" ")
print("years old")