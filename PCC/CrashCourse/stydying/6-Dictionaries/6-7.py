# Using code from previous exercise 
# Storing a person in a dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York',
}
# Adding two new dictionaries
person_2 = {
    'first_name': 'Jane',
    'last_name': 'Smith',
    'age': 25,
    'city': 'Los Angeles',
}
person_3 = {
    'first_name': 'Alice',
    'last_name': 'Johnson',
    'age': 28,
    'city': 'Chicago',
}
# Saving all three dictionaries in a list
people = [person, person_2, person_3]
# Printing all three dictionaries in the list
for person in people:
    print(person)
    # Printing each value in the dictionary
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")