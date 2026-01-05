# Admin
class Admin:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.privileges = []

    def show_privileges(self):
        if self.privileges:
            print(f"Admin {self.username} has the following privileges:")
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print(f"Admin {self.username} has no privileges assigned.")

    def add_privilege(self, privilege):
        self.privileges.append(privilege)
# Example usage
admin_user = Admin("admin1", "admin@example.com")
admin_user.add_privilege("can add post")
admin_user.add_privilege("can delete post")
admin_user.add_privilege("can ban user")
admin_user.show_privileges()
