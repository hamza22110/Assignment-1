# Question 7:
# Distribute Items Equally
# You have n candies and k students.
# Write a program to find:
# 1. How many candies each student gets
# 2. How many candies are left

# Taking inputs from user
n = int(input("Enter the total number of candies: "))
k = int(input("Enter the number of students: "))

# Checking valid input
if k == 0:
    print("Number of students cannot be zero ❌")
else:
    # Calculating distribution
    candies_per_student = n // k
    left_candies = n % k

    # Printing results
    print(f"Each student gets {candies_per_student} candies.")
    print(f"Remaining candies: {left_candies}")

    # Adding logical creativity
    if left_candies == 0:
        print("Perfect distribution 🍬✅")
    elif left_candies == 1:
        print("Only 1 candy is left undistributed 🍭")
    else:
        print(f"{left_candies} candies are left undistributed 🍭")
