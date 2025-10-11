# Exercise 6-4: Glossary 2
# Dictionary with programming words and their meanings
programming_words = {
    'variable': 'a named location used to store data in memory',
    'function': 'a block of organized, reusable code that performs a single action',
    'loop': 'a sequence of instructions that repeats until a condition is met',
    'dictionary': 'a collection of key-value pairs for storing data',
    'list': 'an ordered collection of items which can be of mixed types',
}
# Printing the dictionary

for word, meaning in programming_words.items():
    print(f"{word.title()}: {meaning}")

# Adding a new term to the glossary
programming_words['tuple'] = 'an immutable ordered collection of items'

print("\nUpdated glossary with a new term:")
for word, meaning in programming_words.items():
    print(f"{word.title()}: {meaning}")