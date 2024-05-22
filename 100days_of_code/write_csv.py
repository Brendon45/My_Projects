import csv

def write_data():
    """Function to write data to a CSV file"""
    with open('write.csv', 'w', newline='') as f:
        fieldnames = ["F_name", "L_name", "Rank"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        # Add data to the CSV file here...
        writer.writerow({'Rank': 'B', 'F_name': 'Brendon', 'L_name': 'Jeje'})
        writer.writerow({'Rank': 'A', 'F_name': 'Tafara', 'L_name': 'Nyamhunga'})
        writer.writerow({'Rank': 'B', 'F_name': 'Lawson', 'L_name': 'Redeye'})

    print("Writing complete")

if __name__ == "__main__":
    write_data()
