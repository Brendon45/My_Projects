#!/usr/bin/python3

# This program will identify and print consonants (non-vowels) from a user-provided word.

# Prompt the user to input a word to process.
user_word = input("Enter a word to process here: ")

# Convert the input word to uppercase to handle both uppercase and lowercase vowels.
user_word = user_word.upper()

# Iterate through each letter in the input word.
for letter in user_word:
    # Check if the current letter is a consonant (not a vowel).
    if letter not in "AEIOU":
        # Print the consonant that has not been eaten (removed).
        print("The uneaten consonant is:", letter)