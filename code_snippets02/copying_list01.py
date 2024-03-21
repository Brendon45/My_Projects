#!/usr/bin/env python3

def delete_at(my_list=[], idx=0):
    """
    Delete an element at a specified index in the list.

    Parameters:
    - my_list: The list from which the element will be deleted (default: empty list).    - idx: The index of the element to delete (default: 0).

    Returns:
    - The modified list after deleting the element at the specified index.
    """
    # Check if the index is out of bounds or negative
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the original list if index is invalid
    else:
        del my_list[idx]  # Delete the element at the specified index
        return my_list  # Return the modified list
    
def main():
    # Initialize the list
    my_list = [1, 2, 3, 4, 5]
    
    # Specify the index of the element to delete
    idx = 3
    
    # Call the delete_at function to delete the element at the specified index
    new_list = delete_at(my_list, idx)
    
    # Print the modified list after deletion
    print(new_list)
    
    # Print the original list to show that it's modified in place
    print(my_list)

if __name__ == "__main__":
    main()

