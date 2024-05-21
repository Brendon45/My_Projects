#!/usr/bin/python3
 
# Take input from the user using the input function
# Convert the inputs to float for accurate calculations
Height = float(input("Enter your height in meters: "))
Weight = float(input("Enter your weight in kilograms: "))

# Now let's calculate the BMI of the user
# BMI formula: weight (kg) / (height (m) * height (m))
bmi = Weight / (Height * Height)

# Print the calculated BMI
print(f"Your BMI is: {bmi:.2f}")

# Checking the condition of the user based on BMI value
if bmi < 18.5:
    print("You are underweight. You need to eat healthy.")
elif 18.5 <= bmi < 25:
    print("You are normal weight. Keep it up!")
elif 25 <= bmi < 30:
    print("You are overweight. Please check your diet.")
elif 30 <= bmi < 35:
    print("You are obese. Kindly consider seeing a doctor.")
else:  # This will cover bmi >= 35
    print("You are clinically obese!! Please see a doctor immediately.")
