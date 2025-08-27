# List of pizzas
pizzas = ['pepperoni', 'margherita', 'hawaiian']
# Copy of the list of pizzas
friend_pizzas = pizzas[:]
# Add different pizza to the end of the list
friend_pizzas.append('veggie')
# for loop to print first list
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
# for loop to print friend's list
for pizza in friend_pizzas:
    print(f"My friend likes {pizza} pizza.")