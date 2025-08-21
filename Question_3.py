# Question 3:
# Write a program to calculate Compound Interest.
# Formula: CI = P * (1 + R/100)**T - P

# Taking inputs from user
P = float(input("Enter the Principal amount: "))
R = float(input("Enter the Rate of interest (%): "))
T = float(input("Enter the Time period (in years): "))

# Calculating Compound Interest
CI = P * (1 + R/100)**T - P
total_amount = P + CI

# Printing results
print(f"\nPrincipal: {P}")
print(f"Rate of Interest: {R}%")
print(f"Time: {T} years")
print(f"Compound Interest: {CI}")
print(f"Total Amount after {T} years: {total_amount}")

# Adding logical conditions for creativity
if CI < 1000:
    print("The profit is quite low. Consider increasing rate or time. 📉")
elif CI < 5000:
    print("Good return on investment 👍")
else:
    print("Excellent growth! Your investment worked really well 🚀")
