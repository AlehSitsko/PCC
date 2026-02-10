# Basic dice roll with results stored in a list
import random
# List for storing results of D6 dice rolls
results_d6 = []
# List for storing results of D4 dice rolls
results_d4 = []
# List for storing results of D20 dice rolls
results_d20 = []
# Function to roll a die with a specified number of sides
class dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        result = random.randint(1, self.sides)
        if self.sides == 4:
            results_d4.append(result)
        elif self.sides == 6:
            results_d6.append(result)
        elif self.sides == 20:
            results_d20.append(result)
        return result
# Create instances of different dice
d4 = dice(4)
d6 = dice(6)
d20 = dice(20)
# loop to choice of dice and roll
while True:
    choice = input("Choose a die to roll (d4 = 1, d6 = 2, d20 = 3) or 'p' to print results or 'e' to quit: ")
    if choice == 'e':
        break
    elif choice == '1':
        print(f"You rolled a d4 and got: {d4.roll()}")
    elif choice == '2':
        print(f"You rolled a d6 and got: {d6.roll()}")
    elif choice == '3':
        print(f"You rolled a d20 and got: {d20.roll()}")
    elif choice == 'p':
        print(f"Results of D6 rolls: {results_d6}")
        print(f"Results of D4 rolls: {results_d4}")
        print(f"Results of D20 rolls: {results_d20}")
    else:
        print("Invalid choice. Please choose '1', '2', '3', or 'e'.")
