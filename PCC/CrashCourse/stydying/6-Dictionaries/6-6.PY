# Favorite languages
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',   
    'edward': 'ruby',
    'phil': 'python',
}

# List of people to check
people = ['jen', 'sarah', 'edward', 'phil', 'alice', 'bob']
# Check if each person has taken the poll
for person in people:
    if person in favorite_languages:
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"{person.title()}, please take our poll!")   
# Displaying the favorite languages
print("\nFavorite Languages:")