# List of current items in the receipt
current_items = ['apple', 'banana', 'orange', 'grape']
# Assortment
assortment = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'mango', 'peach', 'pear']

# Items counter (prefill x1 for current_items)
items_counter = {item: 1 for item in current_items}

# Show items for sale (with numbers)
print("Items available for sale:")
for i, item in enumerate(assortment, start=1):
    print(f"{i}. {item}")

# User selects an item
choice = input("Please select a number for the item you want to buy (1-8): ").strip()

# Check user's choice and add to receipt
if choice.isdigit():
    index = int(choice) - 1  # zero-based index
    if 0 <= index < len(assortment):
        selected_item = assortment[index]
        if selected_item in items_counter:
            # already in receipt -> make it x2
            items_counter[selected_item] = 2
            print(f"You already have {selected_item} in your receipt. Changing quantity to x2.")
        else:
            current_items.append(selected_item)
            items_counter[selected_item] = 1
            print(f"{selected_item} has been added to your receipt.")
    else:
        print("Invalid choice. Please select a number between 1 and 8.")
else:
    print("Invalid input. Please enter a number between 1 and 8.")

# Display the current receipt (no duplicates)
print("\nCurrent receipt items and quantities:")
seen = set()
for item in current_items:
    if item not in seen:
        quantity = items_counter.get(item, 1)
        print(f"- {item} x{quantity}")
        seen.add(item)