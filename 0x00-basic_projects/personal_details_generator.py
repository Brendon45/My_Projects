#!/usr/bin/python3

def generate_usernames(first_name, surname):
    # Set to store unique username suggestions
    usernames = set()

    # Generate username suggestions based on different combinations
    # Add suggestion based on first 3 characters of first name and surname
    usernames.add(f"@{first_name[:3].lower()}_{surname[:3].lower()}")

    # Add suggestion based on full first name and surname
    usernames.add(f"@{first_name.lower()}_{surname.lower()}")

    # Add suggestion based on first character of first name and full surname
    usernames.add(f"@{first_name[0].lower()}_{surname.lower()}")

    # Add suggestion based on full first name and first 3 characters of surname
    usernames.add(f"@{first_name.lower()}_{surname[:3].lower()}")

    # Generate additional unique username suggestions (up to 15)
    for i in range(1, len(first_name)):
        for j in range(1, len(surname)):
            usernames.add(f"@{first_name[:i].lower()}_{surname[:j].lower()}")
            if len(usernames) >= 15:
                return usernames

    return usernames

# Input first name and surname
first_name = input("First Name: ")
surname = input("Surname: ")

# Check if both first name and surname are provided
if first_name and surname:
    # Generate and display username suggestions
    usernames = generate_usernames(first_name, surname)
    print(f"Your username suggestions are:")
    for username in usernames:
        print(username)
else:
    print("Please provide both your first name and surname.")
