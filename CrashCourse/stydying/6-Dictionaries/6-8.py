# declaring dictionaries with pets 
pet_1 = {
    'type': 'dog',
    'name': 'Buddy',
    'age': 5,
    'owner': 'John',
}
pet_2 = {
    'type': 'cat',
    'name': 'Whiskers',
    'age': 3,
    'owner': 'Jane',
}
pet_3 = {
    'type': 'parrot',
    'name': 'Polly',
    'age': 2,
    'owner': 'Alice',
}
# saving dictionaries in a list
pets = [pet_1, pet_2, pet_3]
# Looping through the list and printing everything we know about each pet
for pet in pets:
    print(pet)
    print(f"Type: {pet['type']}")
    print(f"Name: {pet['name']}")
    print(f"Age: {pet['age']}")
    print(f"Owner: {pet['owner']}")