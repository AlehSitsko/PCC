# Simple wargame dice roll simulator
import random
# Function to simulate a roll of a six-sided die
def d6():
    return random.randint(1, 6)

# Duel
def duel():
    attacker_hp = 10
    defender_hp = 10
    round_num = 1

    print("Duel Start! Press Enter to roll dice each round.\nFirst to reduce opponent's HP to 0 wins!")

    while attacker_hp > 0 and defender_hp > 0:
        input("Press Enter to roll...")
        atk_roll = d6()
        def_roll = d6()
        print(f"Round {round_num}: Attacker rolls {atk_roll}, Defender rolls {def_roll}")

        if atk_roll > def_roll:
            dmg = atk_roll - def_roll
            defender_hp -= dmg
            print(f"Attacker hits! Defender takes {dmg} damage. Defender HP: {defender_hp}")
        else:
            dmg = def_roll - atk_roll
            attacker_hp -= dmg
            print(f"Defender hits! Attacker takes {dmg} damage. Attacker HP: {attacker_hp}")

        round_num += 1

    print("Duel End!")
    if attacker_hp > 0:
        print("Attacker wins!")
    else:
        print("Defender wins!")
# Start the duel
duel()