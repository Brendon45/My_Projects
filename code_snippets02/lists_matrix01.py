#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Print the elements of a matrix with each row on a new line, separated by spaces.

    Parameters:
    - matrix: The matrix to be printed. Default value is an empty list.

    Returns:
    - None
    """
    for i in matrix:  # Iterate over each row in the matrix
        for j in i:  # Iterate over each element in the row
            if j == i[-1]:  # Check if the element is the last element in the row
                print(j)  # If it's the last element, print it followed by a newline
            else:
                print(j, end=' ')  # If it's not the last element, print it followed by a space

def main():
    # Define a sample matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Call the function to print the matrix
    print_matrix_integer(matrix)

    # Print a separator
    print("--")

    # Call the function with no argument (using default empty matrix)
    print_matrix_integer()

# Call the main function to execute the code
main()
