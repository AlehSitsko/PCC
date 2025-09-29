# Playground 
# Programm to work with dictionaries
# Declaring a dictionary
dict = {}
# User menu for interaction
print("Dictionary Program")
print("You can add key-value pairs to the dictionary.")
# Show instructions
print("Type 'exit' as key to stop adding entries.")
print("Type 'show' to display current dictionary contents.")
# User input to add key-value pairs to the dictionary
while True:
    key = input("Enter key (or 'exit' to stop, 'show' to display): ")
    if key.lower() == 'exit':
        break
    if key.lower() == 'show':
        print("\nCurrent dictionary contents:")
        for k, v in dict.items():
            print(f"{k}: {v}")
        continue
    value = input("Enter value: ")
    dict[key] = value
    print(f"Added: {key} -> {value}")
# Displaying the dictionary
print("\nCurrent dictionary contents:")
for k, v in dict.items():
    print(f"{k}: {v}")
