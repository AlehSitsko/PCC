# Dream Vacation
prompt = "Where would you like to go on vacation? (enter 'quit' to end): "
vacation_spots = []
while True:
    spot = input(prompt)
    if spot.lower() == 'quit':
        break
    vacation_spots.append(spot)
print("The following vacation spots have been added:")
for spot in vacation_spots:
    print(f"- {spot}")