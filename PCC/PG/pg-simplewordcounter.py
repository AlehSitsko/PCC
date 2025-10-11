# Simple word counter, app counts occurrences of each word in input text
import re
from collections import Counter
# Input text from user
input_text = input("Enter text to count words: ")
# Function to count words in a given text
def word_counter(text):
    # Normalize the text to lowercase and split into words
    words = text.lower().split()
    # Remove punctuation from each word
    words = [re.sub(r'[^\w\s]', '', word) for word in words]
    # Use Counter to count occurrences of each word
    word_count = Counter(words)
    return word_count
# Display the word count results
def display_word_count(word_count):
    print("\nWord Count Results:")
    for word, count in word_count.items():
        print(f"{word}: {count}")
# Main function to run the word counter
def main():
    word_count = word_counter(input_text)
    display_word_count(word_count)
# Run the word counter application
if __name__ == "__main__":
    main()