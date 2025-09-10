# List of guests
guests = ["Oleg", "Masha", "Dmitry", "Alena"]
# Invitation message
message = "I would like to invite you to a dinner, "

# Invitation message to everyone
message_to_everyone = "I would like to invite you all to a dinner."
# Print the invitation message
print(f"{message_to_everyone} {guests}.")
# Remove a guest
new_guests = guests.pop(2)  # Remove the third guest

new_message_to_everyone = "Dmitry cannot make it tonight." # Invitation message update
# Update the guest list
print(f"{new_message_to_everyone} {guests}.")