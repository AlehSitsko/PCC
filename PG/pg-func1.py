# Function that accepts the list of numbers, calculates their average, and returns it if it positive if not returns None

#User input: A list of numbers
print("Enter a list of numbers separated by spaces:")
user_input = input()
numbers = list(map(int, user_input.split()))

def average_positive(numbers):
    """Calculate the average of a list of numbers and return it if positive, else return None."""
    if not numbers:
        return None
    
    avg = sum(numbers) / len(numbers)
    
    if avg > 0:
        return avg
    else:
        return None
# Calling the function and displaying the result
result = average_positive(numbers)
if result is not None:
    print(f"The average of the positive numbers is: {result}")
else:
    print("The average of the positive numbers is not available.")