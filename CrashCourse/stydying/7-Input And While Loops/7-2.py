# Restaurant seating
# User input for number of guests
guests = input("Please enter the number of guests: ")
# Setting up integers for guests
guests = int(guests)
# Checking if number of available seats if equal to the number of guests
if guests <= 8:
    print(f"\nTable for {guests} is ready.")
else:
    print(f"\nSorry we dont have a table for {guests} available right now, you will need to wait")
