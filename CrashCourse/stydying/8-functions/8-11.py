# Archived messages
list_of_messages = [
    "Hello, World!",
    "Welcome to the Python Crash Course!",
    "Let's learn about functions.",
    "This is a message from a function."
]
# List of sent messages
sent_messages = []
# List of archived messages
archived_messages = list_of_messages[:]
# Function to send messages
def send_messages(messages):
    """Simulate sending each message."""
    for message in messages[:]:
        print(f"Sending message: {message}")
        list_of_messages.remove(message)
        sent_messages.append(message)
# Call the function to send messages
send_messages(list_of_messages)
# Print both lists to show that messages were moved correctly
print("\nOriginal list of messages:")
for message in list_of_messages:
    print(f"- {message}")
print("\nSent messages:")
for message in sent_messages:
    print(f"- {message}")
# Print archived messages
print("\nArchived messages:")
for message in archived_messages:
    print(f"- {message}")