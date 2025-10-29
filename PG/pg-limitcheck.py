INVENTORY_LIMIT = 100

list_of_items = [
    {"name": "stair_chair", "size": 5},
    {"name": "EAD", "size": 1},
    {"name": "stretcher", "size": 25},
    {"name": "medical_supplies", "size": 35},
    {"name": "cleaning_supplies", "size": 15},
    {"name": "repair_tools", "size": 10}
]

def calculate_total_size(items):
    return sum(item['size'] for item in items)

def check_inventory_space(current_size, new_item_size):
    return current_size + new_item_size <= INVENTORY_LIMIT

print("Current Inventory:")
for item in list_of_items:
    print(f"Name: {item['name']}, Size: {item['size']}")

total_size = calculate_total_size(list_of_items)
print(f"\nInventory limit: {INVENTORY_LIMIT} units")
print(f"Current total size: {total_size} units")

print("\nEnter new item details:")
new_item = {
    "name": input("Enter item name: "),
    "size": int(input("Enter item size: "))
}

if check_inventory_space(total_size, new_item['size']):
    list_of_items.append(new_item)
    total_size = calculate_total_size(list_of_items)
    print("\n✅ New item added.")
else:
    print("\n❌ Not enough space in inventory.")

print(f"\nUpdated total size: {total_size} units")
for item in list_of_items:
    print(f"Name: {item['name']}, Size: {item['size']}")
