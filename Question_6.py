# Question 6:
# Write a program to calculate the Square and Cube of a number.

# Taking input from user
num = float(input("Enter a number: "))

# Calculating square and cube
square = num ** 2
cube = num ** 3

# Printing results
print(f"The square of {num} is: {square}")
print(f"The cube of {num} is: {cube}")

# Adding logical conditions for creativity
if num == 0:
    print("Both square and cube are 0.")
elif num > 0:
    print("You entered a positive number ✅")
else:
    print("You entered a negative number ⚠️")
