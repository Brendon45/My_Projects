#!/usr/bin/python3
# Generate usernames from firstname and surnames

fname = input("First Name: ")
surname = input("Surname: ")

# username = 3fname + _ + 3surname
username = fname[0:3] + '_' + surname[0:3]
print("Your username is", username)