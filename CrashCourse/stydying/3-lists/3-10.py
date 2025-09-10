# List of games
games = ["WoW", "Ashes of Creation", "Elder scrolls Online", "Warhammer RoR"]
# print list of games
print(games)
# Sorted list of games
games_sorted = sorted(games)
# Print the sorted list of games
print(games_sorted)

# Games to play
games_to_play = "Games to play: " + ", ".join(games_sorted)
# Print the games to play
print(games_to_play)

while games:
    games.pop(0)  # Remove the first game
    print("Now playing:", games)
# Print remaining games
print("Remaining games:", games)