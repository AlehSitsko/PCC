# 9-8
#Separate User class
class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

# Separate Privileges class
class Privileges:
    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        if self.privileges:
            print("Privileges:")
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("No privileges assigned.")

    def add_privilege(self, privilege):
        self.privileges.append(privilege)
# Admin class that uses User and Privileges
class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges()
# Example usage
admin_user = Admin("admin1", "Adminson", 35, "admin@example.com")
admin_user.privileges.add_privilege("can add post")
admin_user.privileges.add_privilege("can delete post")
admin_user.privileges.add_privilege("can ban user")
admin_user.privileges.show_privileges()
