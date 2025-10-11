# Dictionary with persons and their favorite numbers
favorite_numbers = {
    'alice': 7,
    'bob': 42,
    'carol': 3,
    'dave': 16,
}
# Printing the dictionary
print(favorite_numbers)
# Printing each person's favorite number
for person, number in favorite_numbers.items():
    print(f"{person.title()}'s favorite number is {number}.")