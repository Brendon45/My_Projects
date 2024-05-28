#!/usr/bin/python3
# this is a guess game program

"""ask user for their guss number"""
num = int(input("Enter a number: "))
guess_num = 3

"""if guss_num == num print you have won"""
if num == guess_num:
    print("you have won")
else:
    print("Incorrect")