# Refrigerator simulation
# This program simulates smart refrigerator, if refrigerator is empty it should be off, else it should be on. 
# It also keeps track of the items in the refrigerator and their quantities.
# Each item has a name and a quantity. The refrigerator can be turned on or off based on whether it contains any items.
# Each item can be added or removed from the refrigerator, and the program will update the status of the refrigerator accordingly.
# The program will also display the current contents of the refrigerator and its status (on or off) when requested and if it on or off
# Each item has its size and the refrigerator has a maximum capacity of 100 units. The program will prevent adding items that would exceed the refrigerator's capacity and will provide feedback to the user when such an attempt is made.
# User can interract with refrigerator via simple loop choice menu, where they can add items, remove items, check the contents of the refrigerator, and check the status of the refrigerator (on or off).
# Define the refrigerator class and its capacity=100
def refrigerator():
    class Refrigerator:
        def __init__(self):
            self.capacity = 100
            self.items = {}
            self.status = "off"

        def add_item(self, name, quantity, size):
            if self.get_total_size() + (quantity * size) > self.capacity:
                print("Cannot add item. Exceeds refrigerator capacity.")
                return
            if name in self.items:
                self.items[name]['quantity'] += quantity
            else:
                self.items[name] = {'quantity': quantity, 'size': size}
            self.update_status()

        def remove_item(self, name, quantity):
            if name not in self.items:
                print("Item not found in refrigerator.")
                return
            if quantity > self.items[name]['quantity']:
                print("Cannot remove item. Not enough quantity.")
                return
            self.items[name]['quantity'] -= quantity
            if self.items[name]['quantity'] == 0:
                del self.items[name]
            self.update_status()

        def get_total_size(self):
            total_size = 0
            for item in self.items.values():
                total_size += item['quantity'] * item['size']
            return total_size

        def update_status(self):
            if len(self.items) > 0:
                self.status = "on"
            else:
                self.status = "off"

        def display_contents(self):
            if len(self.items) == 0:
                print("The refrigerator is empty.")
            else:
                print("Contents of the refrigerator:")
                for name, details in self.items.items():
                    print(f"{name}: Quantity: {details['quantity']}, Size: {details['size']}, Free space: {self.capacity - self.get_total_size()}   units")

        def display_status(self):
            print(f"The refrigerator is currently {self.status}. And it has {self.capacity - self.get_total_size()} free space units.")

    # Create an instance of the Refrigerator class
    fridge = Refrigerator()

    # User interaction loop
    while True:
        print("\nMenu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Check contents")
        print("4. Check status")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            size = int(input("Enter item size: "))
            fridge.add_item(name, quantity, size)
        elif choice == '2':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity to remove: "))
            fridge.remove_item(name, quantity)
        elif choice == '3':
            fridge.display_contents()
        elif choice == '4':
            fridge.display_status()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
# Run the refrigerator simulation
if __name__ == "__main__":    refrigerator() 
