#!/usr/bin/python3

# Prompt user to input number of blocks
block = int(input("Enter the number of blocks: "))

# Initialize block height to zero
height = 0

# Initialize block layer to 1
layer_blocks = 1

# While there are enough blocks to form the next layer
while block >= layer_blocks:
    height += 1  # Increment the height for each completed layer
    block -= layer_blocks  # Reduce the remaining blocks by the current layer's blocks
    layer_blocks += 1  # Increment the number of blocks in the next layer

# Output the height of the pyramid
print("The height of the pyramid is:", height)