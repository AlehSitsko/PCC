# Different Dice roll simulation
import random
class dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)
# Create instances of different dice
d4 = dice(4)
d6 = dice(6)
d20 = dice(20)
# loop to choice of dice and roll
while True:
    choice = input("Choose a die to roll (d4 = 1, d6 = 2, d20 = 3) or 'e' to quit: ")
    if choice == 'e':
        break
    elif choice == '1':
        print(f"You rolled a d4 and got: {d4.roll()}")
    elif choice == '2':
        print(f"You rolled a d6 and got: {d6.roll()}")
    elif choice == '3':
        print(f"You rolled a d20 and got: {d20.roll()}")
    else:
        print("Invalid choice. Please choose '1', '2', '3', or 'e'.")

