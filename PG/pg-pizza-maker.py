# Pizza Order
# Pizza topping list
available_toppings = [
    "pepperoni",
    "mushrooms",
    "green peppers",
    "extra cheese"
]
# Empty list for requested toppings
requested_toppings = []
# User inputs for choosing toppings
print("Welcome to the Pizza Maker!")
print("Available toppings:")
for topping in available_toppings:
    print(f"- {topping}")
while True:
    topping = input("Enter a topping to add (or 'done' to finish): ")
    if topping.lower() == 'done':
        break
    elif topping in available_toppings:
        requested_toppings.append(topping)
        print(f"Added {topping} to your pizza.")
    else:
        print(f"Sorry, we don't have {topping}. Please choose from the available toppings.")
# function to prepare pizza
def prepare_pizza():
    """Simulate preparing a pizza with requested toppings."""
    for topping in requested_toppings:
        print(f"Adding {topping} to your pizza.")
    print(f"Finished preparing your pizza with the following toppings: {', '.join(requested_toppings)}")
# Call the function to prepare pizza
prepare_pizza()