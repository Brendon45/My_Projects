import csv

def writeDict():
    """Open file to write in dictionary format"""
    with open('dict.csv', 'w', newline='') as f:
        fieldnames = ['Name', 'dept', 'birth_month']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # Adding data into the file
        writer.writeheader()
        writer.writerow({'Name': 'Brendon', 'dept': 'IT', 'birth_month': 'Jan'})
        writer.writerow({'Name': 'Tafara', 'dept': 'Game Development', 'birth_month': 'May'})
        writer.writerow({'Name': 'Misheck', 'dept': 'Frontend', 'birth_month': 'Jun'})

    print("Finished writing data")

if __name__ == "__main__":
    writeDict()
