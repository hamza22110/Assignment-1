# Question 17:
# Write a program to convert minutes into hours and minutes.
# Example: 130 minutes → 2 hours 10 minutes

# Taking input from user
minutes = int(input("Enter total minutes: "))

# Validating input
if minutes < 0:
    print("Minutes cannot be negative ❌")
else:
    # Calculations
    hours = minutes // 60
    remaining_minutes = minutes % 60

    # Printing result
    print(f"\n{minutes} minutes = {hours} hour(s) and {remaining_minutes} minute(s)")

    # Adding logical creativity
    if hours == 0:
        print("Less than an hour ⏳")
    elif hours < 5:
        print("That's a few hours of time ⌚")
    else:
        print("That's a long time ⏰")
