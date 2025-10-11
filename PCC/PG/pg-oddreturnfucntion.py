# Function to return odd numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_odd_numbers(num_list):
    odd_numbers = [num for num in num_list if num % 2 != 0]
    return odd_numbers

# Example usage
if __name__ == "__main__":
    print(f"Odd numbers: {get_odd_numbers(numbers)}")# Printing a formatted sentence for each person's favorite number

# Function to return even numbers from a list
def get_even_numbers(num_list):
    even_numbers = [num for num in num_list if num % 2 == 0]
    return even_numbers
# Example usage
if __name__ == "__main__":
    print(f"Even numbers: {get_even_numbers(numbers)}")