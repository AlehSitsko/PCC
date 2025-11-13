# Price Calculation for PG (basically rewrite of my JS Price Calculator for EMS)
# Definition of EMS ride types
EMS_RIDE_TYPES = {
    "BLS": {
        "base_fare": 351,
        "per_km": 13.1,
        "waiting_charge": 100  # per hour
    },
    "ALS": {
        "base_fare": 451,
        "per_km": 13.1,
        "waiting_charge": 100  # per hour
    },
}
# Function to calculate price
def calculate_ems_price(ride_type, distance_km, waiting_time_hours):
    if ride_type not in EMS_RIDE_TYPES:
        raise ValueError("Invalid ride type. Choose 'BLS' or 'ALS'.")
    
    if distance_km < 0 or waiting_time_hours < 0:
        raise ValueError("Distance and waiting time must be non-negative.")
    
    ride_info = EMS_RIDE_TYPES[ride_type]
    base_fare = ride_info["base_fare"]
    distance_charge = ride_info["per_km"] * distance_km
    waiting_charge = ride_info["waiting_charge"] * waiting_time_hours
    
    total_price = base_fare + distance_charge + waiting_charge
    return total_price
# User input for ride type, distance, and waiting time
ride_type = input("Enter ride type (BLS/ALS): ").strip().upper()
distance_km = float(input("Enter distance in km: "))
waiting_time_hours = float(input("Enter waiting time in hours: "))

# Calculate and display the price
try:
    price = calculate_ems_price(ride_type, distance_km, waiting_time_hours)
    print(f"The total price for the {ride_type} ride is: {price}")
except ValueError as e:
    print(e)
