# Simple Phone Book with basic operations
phone_book = {}
# Add a contact
def add_contact(name, number):
    phone_book[name] = number
    print(f"Contact {name} added with number {number}.")
# Get a contact's number
def get_contact(name):
    return phone_book.get(name, "Contact not found.")
# Remove a contact
def remove_contact(name):
    if name in phone_book:
        del phone_book[name]
        print(f"Contact {name} removed.")
    else:
        print("Contact not found.")
# List all contacts
def list_contacts():
    if phone_book:
        for name, number in phone_book.items():
            print(f"{name}: {number}")
    else:
        print("Phone book is empty.")

def main():
    while True:
        print("\nPhone Book Menu:")
        print("1. Add Contact")
        print("2. Get Contact")
        print("3. Remove Contact")
        print("4. List Contacts")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            add_contact(name, number)
        elif choice == '2':
            name = input("Enter contact name to retrieve: ")
            print(get_contact(name))
        elif choice == '3':
            name = input("Enter contact name to remove: ")
            remove_contact(name)
        elif choice == '4':
            list_contacts()
        elif choice == '5':
            print("Exiting phone book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
