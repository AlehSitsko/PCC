# Printing christmas tree line by line
def print_christmas_tree(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
    # Print the trunk
    trunk_width = 1 if height < 3 else 3
    trunk_height = max(1, height // 4)
    trunk_spaces = ' ' * (height - trunk_width // 2 - 1)
    for _ in range(trunk_height):
        print(trunk_spaces + '|' * trunk_width)

# Example usage
if __name__ == "__main__":
    tree_height = 5  # You can change the height for a taller or shorter tree
    print_christmas_tree(tree_height)# Printing christmas tree line by line