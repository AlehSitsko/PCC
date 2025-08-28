# Test for equality and inequality with strings
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Test using the lower() method
print("\nIs car == 'Subaru'? I predict True.")
print(car == 'Subaru')
print("\nIs car == 'AUDI'? I predict False.")
print(car == 'AUDI')

# Numerical test involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
age = 25
print("\nIs age == 25? I predict True.")
print(age == 25)
print("\nIs age == 30? I predict False.")
print(age == 30)
print("\nIs age > 20? I predict True.")
print(age > 20)
print("\nIs age < 30? I predict True.")
print(age < 30)
print("\nIs age >= 25? I predict True.")
print(age >= 25)
print("\nIs age <= 24? I predict False.")
print(age <= 24)

# Test using the and keyword and the or keyword
print("\nIs age > 20 and age < 30? I predict True.")
print(age > 20 and age < 30)
print("\nIs age < 20 or age > 30? I predict False.")
print(age < 20 or age > 30)

# Test whether an item is in the list
fruits = ['apple', 'banana', 'cherry']
print("\nIs 'banana' in the list? I predict True.")
print('banana' in fruits)
print("\nIs 'orange' in the list? I predict False.")
print('orange' in fruits)

# Test whether an item is not in the list
print("\nIs 'grape' not in the list? I predict True.")
print('grape' not in fruits)
print("\nIs 'apple' not in the list? I predict False.")
print('apple' not in fruits)
