#!/usr/bin/python3

def separate_even_odd(my_list):
    """
    Function to separate even and odd numbers from a list.
    
    Args:
    - my_list: List of integers
    
    Returns:
    - Tuple containing two lists: one with even numbers and one with odd numbers
    """
    even_list = []
    odd_list = []
    for i in my_list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list, odd_list

def main():
    list1 = [2, 5, 4, 21, 6, 7]
    print(separate_even_odd(list1))

if __name__ == "__main__":
    main()
