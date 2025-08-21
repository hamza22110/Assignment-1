# Question 4:
# Write a program to calculate the Perimeter of a Rectangle.
# Formula: Perimeter = 2 * (length + width)

# Taking inputs from user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculating perimeter
perimeter = 2 * (length + width)

# Printing result
print(f"The perimeter of the rectangle is: {perimeter}")

# Adding logical conditions for creativity
if length == width:
    print("This is actually a square ⬛")
elif perimeter < 50:
    print("Small rectangle perimeter 📏")
elif perimeter < 150:
    print("Medium rectangle perimeter 📐")
else:
    print("Large rectangle perimeter 🏠")
