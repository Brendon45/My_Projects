#!/usr/bin/python3

"""Copying of lists"""

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
def main():
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = new_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)

main()
