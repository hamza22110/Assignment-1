# Question 13:
# Write a program to calculate the sum of first N natural numbers.
# Formula: sum = n * (n + 1) / 2

# Taking input from user
n = int(input("Enter a number (N): "))

# Calculating sum
if n <= 0:
    print("Please enter a positive number greater than 0 ❌")
else:
    sum_n = n * (n + 1) // 2
    print(f"The sum of first {n} natural numbers is: {sum_n}")

    # Extra logic for creativity
    if n < 10:
        print("That’s a small range of numbers 🙂")
    elif n <= 100:
        print("That’s a decent range of numbers 📊")
    else:
        print("That’s a large range of numbers 🚀")
