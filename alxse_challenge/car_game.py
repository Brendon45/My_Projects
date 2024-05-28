#!/usr/bin/python3
# This is a car game program using a while loop

command = ""  # Initialize the command variable to an empty string
while command != "quit":  # Loop continues until the user types 'quit'
    command = input("> ").lower()  # Get user input and convert it to lowercase
    if command == "start":  # Check if the command is 'start'
        print("car started ...")  # Print a message indicating the car has started
    elif command == "stop":  # Check if the command is 'stop'
        print("car stopped ...")  # Print a message indicating the car has stopped
    elif command == "help":  # Check if the command is 'help'
        # Print the help menu with the available commands
        print("""
start ...... to start the car
stop ....... to stop the car
quit ....... to quit
        """)
    elif command == "quit":  # Check if the command is 'quit'
        break  # Exit the loop
    else:  # If the command is not recognized
        print("Sorry, I don't understand")  # Print an error message
