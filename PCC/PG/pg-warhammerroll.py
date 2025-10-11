# Warhammer 40k Dice Roller
import random
# input fields for attacker unit
attacker_unit = input("Enter attacker unit name: ")
attacker_ws = int(input("Enter attacker weapon skill (1-6): "))
attacker_bs = int(input("Enter attacker ballistic skill (1-6): "))
attacker_str = int(input("Enter attacker strength (1-10): "))
attacker_toughness = int(input("Enter attacker toughness (1-10): "))

# input fields for defender unit
defender_unit = input("Enter defender unit name: ")
defender_ws = int(input("Enter defender weapon skill (1-6): "))
defender_bs = int(input("Enter defender ballistic skill (1-6): "))
defender_str = int(input("Enter defender strength (1-10): "))
defender_toughness = int(input("Enter defender toughness (1-10): "))

# Dice roll function
def roll_dice():
    return random.randint(1, 6)

# Function to determine hits
def determine_hits(roll, skill):
    return roll >= skill
# Function to determine wounds
def determine_wounds(roll, strength, toughness):
    if strength >= toughness * 2:
        required_roll = 2
    elif strength > toughness:
        required_roll = 3
    elif strength == toughness:
        required_roll = 4
    elif strength < toughness:
        required_roll = 5
    else:  # strength * 2 <= toughness
        required_roll = 6
    return roll >= required_roll
# Function to determine saves
def determine_saves(roll, save):
    return roll >= save
# Function to calculate damage
def calculate_damage(wounds, damage_per_wound):
    return wounds * damage_per_wound    
# Main combat simulation
def combat_simulation():
    print(f"\n{attacker_unit} attacks {defender_unit}!")
    
    # Melee attack phase
    melee_roll = roll_dice()
    print(f"{attacker_unit} rolls a {melee_roll} to hit (WS {attacker_ws})")
    if determine_hits(melee_roll, attacker_ws):
        print("Hit!")
        wound_roll = roll_dice()
        print(f"Rolling to wound: {wound_roll} (Str {attacker_str} vs Tough {defender_toughness})")
        if determine_wounds(wound_roll, attacker_str, defender_toughness):
            print("Wound!")
            save_roll = roll_dice()
            defender_save = 3  # Example save value
            print(f"{defender_unit} rolls a {save_roll} to save (Save {defender_save})")
            if not determine_saves(save_roll, defender_save):
                damage = calculate_damage(1, 1)  # Example damage per wound
                print(f"{defender_unit} takes {damage} damage!")
            else:
                print(f"{defender_unit} saves the wound!")
        else:
            print("No wound.")
    else:
        print("Missed!")

combat_simulation()