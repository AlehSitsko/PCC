# Dictionary with programming words and their meanings
programming_words = {
    'variable': 'a named location used to store data in memory',
    'function': 'a block of organized, reusable code that performs a single action',
    'loop': 'a sequence of instructions that repeats until a condition is met',
    'dictionary': 'a collection of key-value pairs for storing data',
    'list': 'an ordered collection of items which can be of mixed types',
}
# Printing the dictionary
print(programming_words)
# Printing each word and its meaning
for word, meaning in programming_words.items():
    print(f"{word.title()}: {meaning}")
# Printing a formatted sentence for each word
for word, meaning in programming_words.items():
    print(f"The term '{word}' means: {meaning}.")