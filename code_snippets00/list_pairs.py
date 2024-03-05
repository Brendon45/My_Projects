#!/usr/bin/python3

# Define a function to find pairs of elements with equal values in a list
def getPairs(myList):
    # Iterate over each element in the list
    for i in range(0, len(myList)):
        # Iterate over the remaining elements after the current element
        for j in range(i + 1, len(myList)):
            # Check if the current element and the next elements have the same value
            if (myList[i] == myList[j]):
                # If a pair is found, print the information about the pair
                print(
                    "Number " + str(myList[i]) +
                    " is included two times, at indices " +
                    str(i) + " and " + str(j)
                )
# Example list to test the function
myList = [1, 3, 4, 6, 1, 9, 4, 8, 9]
# Call the function to find pairs in the list
getPairs(myList)