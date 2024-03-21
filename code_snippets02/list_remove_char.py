#!/usr/bin/python3

def no_c(my_string):
    """
    Remove all occurrences of the characters 'c' and 'C' from a given string.

    Parameters:
    - my_string: The input string.

    Returns:
    - None (the function prints the modified string).
    """
    # Iterate through each character in the string
    for character in my_string:
        # Check if the current character is not 'c' or 'C'
        if character not in "Cc":
            # If it's not 'c' or 'C', print it without newline
            print(character, end='')

def main():
    # Test the function with different input strings
    no_c("Best School")  # Output: "Best Shool"
    no_c("Chicago")      # Output: "hiago"
    no_c("C is fun!")    # Output: " is fun!"

# Call the main function to execute the code
main()
