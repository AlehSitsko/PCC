# Dice roll mini project
import random

roll = input("Roll the die? (y/n): ").strip().lower()

if roll == 'beer':
    print("Cheers! Enjoy your beer surprise! 🍺")
    exit()

if roll != 'y':
    print("Dice roll cancelled.")
    exit()

# Simulate rolling a six-sided die
dice_roll = random.randint(1, 6)

# Display the result
if dice_roll == 1:
    print("You rolled 1! Critical Fail! 💀")
elif dice_roll == 6:
    print("You rolled 6! Critical Success! 🎯")
else:
    print(f"You rolled a {dice_roll}.")
