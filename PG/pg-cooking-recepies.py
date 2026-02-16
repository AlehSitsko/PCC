# Lightweight programm to write, store and print cooking recepies
# User interraction is done via command line interface ex 1 show recepies, ex 2 add recepie, ex 3 delete recepie, ex 4 exit program
# recepies are stored in a dictionary with the name of the recepie as key and the ingredients and instructions as values
recepies = {}
# Function to interact with the user
def print_menu():
    print("<==== Cooking Recepies Menu ===>")
    print("Please select an option:")
    print("1. Show recepies")
    print("2. Add recepie")
    print("3. Delete recepie")
    print("4. View recepie")
    print("5. Edit recepie")
    print("6. Exit program")

# Function to show all recepies
def show_all_recepies():
    if not recepies:
        print("No recepies found.")
        return
    
    print("All recepies:")
    for i, name in enumerate(recepies, start=1):
        print(f"{i}. {name}")

# Function to add a recepie
def add_recepie():
    name = input("Enter the name of the recepie: ")
    ingredients = input("Enter the ingredients (separated by commas): ")
    instructions = input("Enter the instructions: ")
    
    recepies[name] = {
        "ingredients": [ingredient.strip() for ingredient in ingredients.split(",")],
        "instructions": instructions
    }
    print(f"Recepie '{name}' added successfully.")

# Function to delete a recepie
def delete_recepie():
    if not recepies:
        print("No recepies found.")
        return

    show_all_recepies()
    try:
        choice = int(input("Enter the number of the recepie you want to delete: "))
        names = list(recepies.keys())
        if 1 <= choice <= len(names):
            name = names[choice - 1]
            del recepies[name]
            print(f"Recepie '{name}' deleted successfully.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

# Function to view one recepie
def view_one_recepie():
    if not recepies:
        print("No recepies found.")
        return

    show_all_recepies()
    try:
        choice = int(input("Enter the number of the recepie you want to view: "))
        names = list(recepies.keys())
        if 1 <= choice <= len(names):
            name = names[choice - 1]
            details = recepies[name]
            print(f"Recepie: {name}")
            print(f"Ingredients: {details['ingredients']}")
            print(f"Instructions: {details['instructions']}")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")
# Function to edit a recepie
def edit_recepie():
    if not recepies:
        print("No recepies found.")
        return

    show_all_recepies()
    try:
        choice = int(input("Enter the number of the recepie you want to edit: "))
        names = list(recepies.keys())
        if 1 <= choice <= len(names):
            name = names[choice - 1]
            details = recepies[name]
            print(f"Editing recepie: {name}")
            new_name = input(f"Enter new name (or press Enter to keep '{name}'): ")
            new_ingredients = input(f"Enter new ingredients (separated by commas) (or press Enter to keep current): ")
            new_instructions = input(f"Enter new instructions (or press Enter to keep current): ")

            if new_name:
                recepies[new_name] = recepies.pop(name)
                name = new_name
            if new_ingredients:
                recepies[name]['ingredients'] = [ingredient.strip() for ingredient in new_ingredients.split(",")]
            if new_instructions:
                recepies[name]['instructions'] = new_instructions
            
            print(f"Recepie '{name}' updated successfully.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")
# Main loop
def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            show_all_recepies()
        elif choice == '2':
            add_recepie()
        elif choice == '3':
            delete_recepie()
        elif choice == '4':
            view_one_recepie()
        elif choice == '5':
            edit_recepie()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
# Run the main loop
if __name__ == "__main__":    main()
