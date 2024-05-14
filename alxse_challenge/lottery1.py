#!/usr/bin/python3

# The draw from the lottery organization
lotteryDraw = [98, 1, 59, 70, 37, 4]

# Ask the user to enter their picks
print("Enter your lottery picks (6 numbers between 1 and 98):")
picks = []
for i in range(6):
    while True:
        try:
            pick = int(input(f"Enter pick {i+1}: "))
            if 1 <= pick <= 98:  # Validate that the pick is within the valid range
                picks.append(pick)
                break
            else:
                print("Please enter a number between 1 and 98.")
        except ValueError:
            print("Please enter a valid integer.")

# Count the number of matching picks with the lottery draw
matches = sum(1 for number in picks if number in lotteryDraw)

# Display the number of matches
print(f"You matched {matches} number(s) with the lottery draw numbers.")