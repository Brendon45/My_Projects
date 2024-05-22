# Open a file in write and read mode
with open("brendon.txt", "w+") as file:
    # Write to the file
    file.write("Hello, Brendon! I hope you are doing well.")
    
    # Move the pointer of the file object to the beginning of the file
    file.seek(0)
    
    # Print what is in the file
    print("Content after initial write:")
    print(file.read())

# Adding some more content using append mode
with open("brendon.txt", "a") as file2:
    file2.write("\nHow are you?")

# Printing all content in the file
with open("brendon.txt", "r") as f:
    lines = f.readlines()
    print("\nContent after appending:")
    for line in lines:
        print(line.strip())