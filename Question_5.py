# Question 5:
# Write a program to calculate the average of three numbers.

# Taking inputs from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculating average
average = (num1 + num2 + num3) / 3

# Printing result
print(f"The average of {num1}, {num2}, and {num3} is: {average}")

# Adding logical conditions for creativity
if average > 75:
    print("The average is High 📈")
elif average >= 40:
    print("The average is Moderate 📊")
else:
    print("The average is Low 📉")
