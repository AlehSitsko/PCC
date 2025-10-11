# Minigame Phalanx Fight, two units of 100 soldiers each, each plalanx unit stands in formation of 10 rows and 10 columns
# Each soldier roll a d6 dice, and the highest total wins
# after dying each soldier in the line of phalanx is removed, and the next soldier in line takes his place
import random
# Unit class to represent a phalanx unit
class PhalanxUnit:
    def __init__(self, name):
        self.name = name
        self.soldiers = [1] * 100  # Each soldier represented by 1, total 100 soldiers
    def is_defeated(self):
        return len(self.soldiers) == 0
    def lose_soldiers(self, count):
        # Remove soldiers from the front (line) of the phalanx
        del self.soldiers[:count]
    def soldier_count(self):
        return len(self.soldiers)

def roll_dice(num_dice=6, sides=6):
    return sum(random.randint(1, sides) for _ in range(num_dice))

def fight_round(unit1, unit2):
    if unit1.is_defeated() or unit2.is_defeated():
        return None  # No fight if any unit is defeated
    roll1 = roll_dice()
    roll2 = roll_dice()
    if roll1 > roll2:
        unit2.lose_soldiers(1)
        return unit1.name
    elif roll2 > roll1:
        unit1.lose_soldiers(1)
        return unit2.name
    else:
        # Tie: both lose one soldier
        unit1.lose_soldiers(1)
        unit2.lose_soldiers(1)
        return "Tie"

def simulate_battle(unit1, unit2):
    print(f"Battle start: {unit1.name} vs {unit2.name}")
    round_num = 1
    while not unit1.is_defeated() and not unit2.is_defeated():
        winner = fight_round(unit1, unit2)
        print(f"Round {round_num}: {unit1.name} ({unit1.soldier_count()}) vs {unit2.name} ({unit2.soldier_count()}) - ", end="")
        if winner == "Tie":
            print("Tie, both lose 1 soldier")
        elif winner is None:
            print("Battle ended")
            break
        else:
            print(f"{winner} wins the round")
        round_num += 1
    if unit1.is_defeated() and unit2.is_defeated():
        print("The battle ended in a draw. Both units are defeated.")
    elif unit1.is_defeated():
        print(f"{unit2.name} wins the battle!")
    else:
        print(f"{unit1.name} wins the battle!")

if __name__ == "__main__":
    phalanx1 = PhalanxUnit("Sparta")
    phalanx2 = PhalanxUnit("Athens")
    simulate_battle(phalanx1, phalanx2)