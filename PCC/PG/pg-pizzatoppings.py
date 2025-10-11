# pizza toppings but with printing full list of toppings after quitting
prompt = "Enter a pizza topping you want (enter 'quit' to end): "
toppings = []
while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    else:
        toppings.append(topping)
        print(f"I'll add {topping} to your pizza.")
print("Your pizza has the following toppings:")
for topping in toppings:
    print(f"- {topping}")
