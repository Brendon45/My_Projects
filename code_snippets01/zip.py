#!/usr/bin/python3

# List of user IDs
user_id = ["12132", "56723", "32145", "23456"]

# List of user names
user_name = ["Brian", "Simon", "Tafara", "Misheck"]

# Combine user names and IDs into tuples using zip
user_info = list(zip(user_name, user_id))

# Print the list of user information
print(user_info)