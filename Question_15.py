# Question 15:
# Write a program to calculate speed.
# Formula: Speed = Distance / Time

# Taking inputs from user
distance = float(input("Enter the distance (in km): "))
time = float(input("Enter the time (in hours): "))

# Checking valid input
if time <= 0:
    print("Time must be greater than 0 ❌")
else:
    # Calculating speed
    speed = distance / time

    # Printing result
    print(f"\nDistance: {distance} km")
    print(f"Time: {time} hours")
    print(f"Speed: {speed:.2f} km/h")

    # Adding logical conditions for creativity
    if speed < 20:
        print("You are moving very slow 🚶")
    elif speed <= 80:
        print("You are moving at a normal speed 🚗")
    else:
        print("You are moving very fast 🚀")
