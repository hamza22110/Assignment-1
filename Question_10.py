# Question 10:
# Write a program to calculate Salary.
# Input basic salary. Calculate:
# - HRA = 20% of basic
# - DA = 15% of basic
# - Total Salary = Basic + HRA + DA

# Taking input from user
basic_salary = float(input("Enter the Basic Salary: "))

# Calculations
hra = 0.20 * basic_salary
da = 0.15 * basic_salary
total_salary = basic_salary + hra + da

# Printing results
print(f"\nBasic Salary: {basic_salary}")
print(f"HRA (20%): {hra}")
print(f"DA (15%): {da}")
print(f"Total Salary: {total_salary}")

# Adding logical conditions for creativity
if total_salary > 100000:
    print("You are earning a high salary 💰🚀")
elif total_salary >= 50000:
    print("You are earning a decent salary 🙂")
else:
    print("You are earning a modest salary, keep growing 📈")
