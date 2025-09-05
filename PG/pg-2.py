# basic programm to see if warehouse is empty
# Define the warehouse capacity
warehouse_capacity = 1000
# Warehouse - 100 items unloaded
warehouse_unloaded = 100
# Calculate the current stock in the warehouse
current_stock = warehouse_capacity - warehouse_unloaded
# Input question to user
question = input("Do you want to unload 1 unit? (yes/no): ").strip().lower()
# Check if the user wants to unload an item
if question == 'yes':
    if current_stock > 0:
        current_stock = warehouse_capacity - warehouse_unloaded
        # Print the current stock after unloading
        print("1 unit unloaded. Current stock:", current_stock)
    else:
        print("Cannot unload. The warehouse is empty.")
# Check if the warehouse is empty
if current_stock == 0:
    print("The warehouse is empty.")

# Check if the warehouse is not empty
if current_stock != 0:
    print("The warehouse is not empty.")