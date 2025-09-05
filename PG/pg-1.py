# Simple program to calculate ETA

# Average speed definition
avg_speed = 35  # in miles per hour
# Distance to travel need to be input by user
distance = float(input("Enter the distance to travel (in miles): "))
# Calculate ETA in hours(formated to 2 decimal places)
eta = distance / avg_speed
# Display the ETA
print(f"Estimated Time of Arrival (ETA): {eta:.2f} hours")