# importing necessary libraries
import random
n = random.randint(1, 6)

# Player stats for calculations
player = {
    "strength": 10,
    "agility": 12,
    "intelligence": 14
}

# Enemy stats for calculations
enemy = {
    "strength": 8,
    "agility": 10,
    "intelligence": 12
}
# Function to simulate a dice roll
def roll_dice(sides=6):
    """Simulate rolling a dice with a given number of sides."""
    return random.randint(1, sides)
# Function to calculate damage based on player and enemy stats
def calculate_damage(player, enemy):
    """Calculate damage dealt by player to enemy based on their stats."""
    base_damage = roll_dice()
    damage = base_damage + (player["strength"] - enemy["agility"]) // 2
    return max(damage, 0)  # Ensure damage is not negative
# Simulating an attack
damage_dealt = calculate_damage(player, enemy)
print(f"Damage dealt to the enemy: {damage_dealt}")
