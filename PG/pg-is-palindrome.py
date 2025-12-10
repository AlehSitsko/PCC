# Simple Palindrome Checker
# Input from user
input_str = input("Enter a string to check if it's a palindrome: ")
# Check if the string is a palindrome
if input_str == input_str[::-1]:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

# print input in reverse order
print("Reversed string:", input_str[::-1])