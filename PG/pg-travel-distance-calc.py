# small function to calculate travel distance per day by user input of morning odometer and evening odometer readings
# Storing data
travel_data = []
# User input: Morning and evening odometer readings
def calculate_travel_distance(morning_reading, evening_reading):
    """Calculate the travel distance for the day."""
    return evening_reading - morning_reading
print("Enter the morning odometer reading:")
morning_input = float(input())
print("Enter the evening odometer reading:")
evening_input = float(input())  
# Calling the function and displaying the result
distance_traveled = calculate_travel_distance(morning_input, evening_input)
print(f"Distance traveled today: {distance_traveled} miles")
# Storing the data
travel_data.append({
    "morning": morning_input,
    "evening": evening_input,
    "distance": distance_traveled
})
# Displaying all travel data
print("Travel Data:")
for entry in travel_data:
    print(f"Morning: {entry['morning']}, Evening: {entry['evening']}, Distance: {entry['distance']} miles")