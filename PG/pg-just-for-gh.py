# TO BE COMPLETED
# EASY SCRIPT FOR COLLECTING USER DATA AND STORING IN A LIST
# REPEATEDLE INPUT FOR DATA COLLECTION
user_data = []
while True:
    name = input("Enter your name (or type 'exit' to finish): ")
    if name.lower() == 'exit':
        break
    age = input("Enter your age: ")
    city = input("Enter your city: ")
    user_data.append({'name': name, 'age': age, 'city': city})
# DISPLAY COLLECTED DATA
print("\nCollected User Data:")
for user in user_data:
    print(f"Name: {user['name']}, Age: {user['age']}, City: {user['city']}")
    