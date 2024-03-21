#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Print the elements of a matrix with each row on a new line, separated by spaces.

    Parameters:
    - matrix: The matrix to be printed. Default value is an empty list.

    Returns:
    - None
    """
    # Iterate over each row in the matrix
    for i in matrix:
        # Iterate over each element in the row
        for j in i:
            # Check if the element is the last element in the row
            if j == i[-1]:
                # If it's the last element, print it followed by a newline
                print(f"{j}$")
            else:
                # If it's not the last element, print it followed by a space
                print(j, end=' ')

def main():
    # Define a matrix as a list of lists
    my_list = [[1, 2, 3, 9], [4, 5, 6], [7, 8, 9, 0, 13]]
    # Call the function to print the matrix
    print_matrix_integer(my_list)

# Call the main function to execute the code
main()
