#!/usr/bin/python3

def greet_user(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    

# greet_user("Obed")
greet_user(fname="obed", lname="Ehoneah")