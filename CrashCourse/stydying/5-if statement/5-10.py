# Programm that simuldates how websites ensure that user has unique usernames
# List of current usernames
current_users = ['alice', 'bob', 'charlie', 'david', 'eve']
# List of new usernames to be registered
new_users = ['Eve', 'frank', 'Grace', 'bob', 'heidi']
# Loop through new users to check for uniqueness (case-insensitive)
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a different username.")
    else:
        print(f"The username '{new_user}' is available.")