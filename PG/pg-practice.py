# Some python practice 
# Input to collect user data and save to a dictionary
user_data = {}
user_data['first_name'] = input("Enter your first name: ")
user_data['last_name'] = input("Enter your last name: ")
user_data['age'] = int(input("Enter your age: "))
user_data['email'] = input("Enter your email address: ")
# Display the collected user data
print("Collected User Data:")
for key, value in user_data.items():
    print(f"{key.capitalize()}: {value}")
# Simple function to greet the user
def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python practice program.")
greet_user(user_data['first_name'])