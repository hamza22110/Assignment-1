# Question 11:
# Write a program to calculate Age in Months and Days.
# Input age in years and calculate:
# - Age in months
# - Age in days (approximate)

# Taking input from user
age_years = int(input("Enter your age in years: "))

# Calculations
age_months = age_years * 12
age_days = age_years * 365   # Approximate (ignores leap years)

# Printing results
print(f"\nYour age in months: {age_months}")
print(f"Your age in days (approximate): {age_days}")

# Adding logical conditions for creativity
if age_years < 13:
    print("You are a Child 👶")
elif age_years < 20:
    print("You are a Teenager 👦👧")
elif age_years < 60:
    print("You are an Adult 🧑")
else:
    print("You are a Senior 👴👵")
