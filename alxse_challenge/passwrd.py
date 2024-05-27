#!/usr/bin/python3
"""Login authentication"""

username = "admin"
password = "TeN23z#!"

print("Welcome to my awesome app")
user_username = input("Username: ").lower()
user_password = input("Password: ")

if (user_username == username and user_password == password):
    print("Successfully logged in")
elif (user_username == username):
    print("Wrong password")
else:
    print("Username doesn't exist")