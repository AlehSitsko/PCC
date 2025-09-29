# Dictionary with persons and their favorite numbers
favorite_numbers = {
    'alice': [7, 12],
    'bob': [42, 99],
    'carol': [3, 14],
    'dave': [16, 23],
}
# Printing the dictionary
print(favorite_numbers)
# Printing each person's favorite numbers
for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers are: {', '.join(map(str, numbers))}.")