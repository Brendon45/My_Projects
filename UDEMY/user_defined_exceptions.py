# Tutorial 28-Python User Defined Exception

# Define a custom exception for voter's eligibility
class VotersElligibility(Exception):
    def __init__(self):
        super().__init__()

# Try block to handle user input and check eligibility
try:
    # Get the user's age and convert it to an integer
    age = int(input("Enter your age: "))
    print("Age is " + str(age))
    
    # Check if age is less than 18
    if age < 18:
        # Raise custom exception if age is less than 18
        raise VotersElligibility

# Handle the custom VotersElligibility exception
except VotersElligibility:
    print("Age is less than 18")

# Handle the ValueError exception if input is not an integer
except ValueError:
    print("Age is not numeric")

# Execute if no exceptions were raised
else:
    print("Age is greater than or equal to 18")

# Finally block to execute regardless of exceptions
finally:
    print("End of the program")
