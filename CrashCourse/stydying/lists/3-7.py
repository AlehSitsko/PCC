# List of guests
guests = ["Oleg", "Masha", "Dmitry", "Alena"]
# Invitation message
print("We found a bigger table. We can invite more people.", guests)
# Update the guest list
guests.insert(0, "Alex")
guests.insert(2, "John")
guests.append("Kate")
# Print the updated guest list
print("Updated guest list:", guests)

# Message with informing about removing from list
print("Unfortunately, you were uninvited to dinner.", guests.pop(6))  # Uninviting Kate
print("Unfortunately, you were uninvited to dinner.", guests.pop(5))  # Uninviting Alena
print("Unfortunately, you were uninvited to dinner.", guests.pop(4))  # Uninviting Dmitry
print("Unfortunately, you were uninvited to dinner.", guests.pop(3))  # Uninviting John
print("Unfortunately, you were uninvited to dinner.", guests.pop(2))  # Uninviting Alex
# Print invitations for the remaining guests
print(f"Hello {guests}, you are invited to dinner!")
# Printing remaining guests
print(guests)

# Deleting guests
del guests[0]  # Remove Alex
del guests[0]  # Remove Oleg
# Printing clear list
print(guests)  # Should be empty now