# Question 8:
# Write a program to calculate Profit or Loss.
# Input cost price (CP) and selling price (SP).
# Display either:
#Profit and amount
#Loss and amount
#No Profit No Loss

# Taking inputs from user
cost_price = float(input("Enter the Cost Price (CP): "))
selling_price = float(input("Enter the Selling Price (SP): "))

# Checking profit or loss
if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"✅ You made a Profit of {profit}")
    if profit > 1000:
        print("Great job! Huge profit 🚀")
    else:
        print("Decent profit 👍")
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print(f"⚠️ You incurred a Loss of {loss}")
    if loss > 1000:
        print("Warning! Big loss 😢")
    else:
        print("Small loss, try again next time 📉")
else:
    print("No Profit No Loss – you broke even 😐")
