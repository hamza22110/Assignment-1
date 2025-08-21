# Question 1:
# Write a program that converts a temperature from Celsius to Fahrenheit. 
# (Formula: Fahrenheit = (Celsius * 9/5) + 32)

# Taking input from the user
celsius = float(input("Enter temperature in Celsius: "))

# Applying formula
fahrenheit = (celsius * 9/5) + 32

# Printing result
print(f"{celsius}°C is equal to {fahrenheit}°F")

# Adding logical conditions to describe the weather
if celsius < 0:
    print("It's freezing cold! ❄️")
elif celsius < 15:
    print("The weather is quite cool 🧥")
elif celsius < 25:
    print("It's a pleasant day 🌤️")
elif celsius < 35:
    print("The weather is warm ☀️")
else:
    print("It's really hot 🔥")
