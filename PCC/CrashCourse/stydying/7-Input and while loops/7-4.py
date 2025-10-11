# Pizza toppings
prompt = "Enter a pizza topping you want (enter 'quit' to end): "
while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")
        