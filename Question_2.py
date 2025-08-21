# Question 2:
# Write a program to calculate the Area of a Rectangle.

# Taking input from user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculating area
area = length * width

# Printing result
print(f"The area of the rectangle is: {area}")

# Adding logical conditions for creativity
if length == width:
    print("This is not just a rectangle, it's a Square! ⬛")
elif area < 50:
    print("This is a small rectangle 📏")
elif area < 200:
    print("This is a medium-sized rectangle 📐")
else:
    print("This is a large rectangle 🏠")
