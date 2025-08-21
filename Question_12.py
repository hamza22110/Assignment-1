# Question 12:
# Write a program to convert currency from USD to PKR.
# Input amount in USD and convert using a fixed exchange rate.

# Taking input from user
usd = float(input("Enter amount in USD: "))

# Fixed exchange rate (example: 1 USD = 280 PKR)
exchange_rate = 280  

# Conversion
pkr = usd * exchange_rate

# Printing result
print(f"{usd} USD is equal to {pkr} PKR")

# Adding logical conditions for creativity
if usd < 10:
    print("That's a small amount 💵")
elif usd <= 100:
    print("That's a decent amount of money 💰")
else:
    print("Wow, that's a big amount of money 🚀")
