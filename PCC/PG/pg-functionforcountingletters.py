# Function to count letters in a string
# Example string
string = "Hello, World!"

# Function to count letters
def count_letters(s):
    count_letters = sum(1 for char in s if char.isalpha())
    return count_letters

# Example usage
if __name__ == "__main__":
    print(f"Number of letters: {count_letters(string)}")

# Function to count vowels in a string
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count_vowels = sum(1 for char in s if char in vowels)
    return count_vowels

# Example usage
if __name__ == "__main__":
    print(f"Number of vowels: {count_vowels(string)}")

# Function to count consonants in a string
def count_consonants(s):
    vowels = 'aeiouAEIOU'
    count_consonants = sum(1 for char in s if char.isalpha() and char not in vowels)
    return count_consonants
# Example usage
if __name__ == "__main__":
    print(f"Number of consonants: {count_consonants(string)}")