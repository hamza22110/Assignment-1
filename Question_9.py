# Question 9:
# Write a program to calculate:
# - Total Marks
# - Percentage
# - Average
# Input marks of 5 subjects

# Taking inputs from user
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

# Assuming each subject is out of 100
total_marks = m1 + m2 + m3 + m4 + m5
percentage = (total_marks / 500) * 100
average = total_marks / 5

# Printing results
print(f"\nTotal Marks = {total_marks}")
print(f"Percentage = {percentage}%")
print(f"Average Marks = {average}")

# Adding logical grading system
if percentage >= 80:
    print("Grade: A+ 🏆 Excellent performance!")
elif percentage >= 70:
    print("Grade: A 🎉 Great job!")
elif percentage >= 60:
    print("Grade: B 🙂 Good effort!")
elif percentage >= 50:
    print("Grade: C ⚠️ Needs improvement.")
else:
    print("Grade: F ❌ Failed. Work harder next time!")
