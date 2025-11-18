# Users
class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        
    def describe_user(self):
        print(f"User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")
# Example usage task 9-3
# 1st user
user1 = User("Alice", "Smith", 30, "alice@example.com")
user1.describe_user()
user1.greet_user()
# 2nd user
user2 = User("Bob", "Johnson", 25, "bob@example.com")
user2.describe_user()
user2.greet_user()
# 3rd user
user3 = User("Charlie", "Brown", 28, "charlie@example.com")
user3.describe_user()
user3.greet_user()