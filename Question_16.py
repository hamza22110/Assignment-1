# Question 16:
# Write a program to calculate Body Mass Index (BMI).
# Formula: BMI = weight / (height ** 2)

# Taking inputs from user
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Validating input
if height <= 0:
    print("Height must be greater than 0 ❌")
else:
    # Calculating BMI
    bmi = weight / (height ** 2)

    # Printing result
    print(f"\nYour BMI is: {bmi:.2f}")

    # Adding logical conditions for BMI categories
    if bmi < 18.5:
        print("You are Underweight ⚠️")
    elif bmi < 24.9:
        print("You have a Normal weight ✅")
    elif bmi < 29.9:
        print("You are Overweight ⚠️")
    else:
        print("You are Obese ❌")
