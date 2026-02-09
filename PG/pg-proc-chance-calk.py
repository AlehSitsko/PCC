# Simple calculator to check the chances of spell proc or critical strike proc on hit.
def proc_chance(chance, hits):
    proc_chance = 1 - (1 - chance) ** hits
    return proc_chance
# Get user input for proc chance and number of hits
try:
    chance = float(input("Enter the proc chance (as a decimal, e.g., 0.25 for 25%): "))
    hits = int(input("Enter the number of hits: "))
    if 0 <= chance <= 1 and hits >= 0:
        result = proc_chance(chance, hits)
        print(f"The chance of at least one proc occurring in {hits} hits is: {result:.2%}")
    else:
        print("Please enter a valid proc chance (0-1) and a non-negative number of hits.")
except ValueError:    print("Invalid input. Please enter a decimal for proc chance and an integer for hits.")
