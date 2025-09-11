# Function that finds the biggest and lowest number in a list
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

def find_biggest_and_lowest(num_list):
    if not num_list:
        return None, None
    biggest = max(num_list)
    lowest = min(num_list)
    return biggest, lowest

# Example usage
if __name__ == "__main__":
    biggest, lowest = find_biggest_and_lowest(numbers)
    print(f"Biggest number: {biggest}")
    print(f"Lowest number: {lowest}")