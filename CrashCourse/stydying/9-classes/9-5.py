# taks 9-5
# Users with added attribute for login attempts
class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Login Attempts: {self.login_attempts}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        
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
user1.increment_login_attempts()

# 2nd user
user2 = User("Bob", "Johnson", 25, "bob@example.com")
user2.describe_user()
user2.greet_user()
user2.increment_login_attempts()
# 3rd user
user3 = User("Charlie", "Brown", 28, "charlie@example.com")
user3.describe_user()
user3.greet_user()
user3.increment_login_attempts()
# Display login attempts
print("\nLogin Attempts:")
user1.describe_user()   
user2.describe_user()
user3.describe_user()
# Reset login attempts for user1
user1.reset_login_attempts()
print("\nAfter resetting login attempts for user1:")
user1.describe_user()
user2.describe_user()
user3.describe_user()

