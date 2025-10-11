# Three Exits
prompt = "Enter a pizza topping you want (enter 'quit' to end): "
toppings = []
while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    elif topping.lower() == 'exit':
        break
    elif topping.lower() == 'stop':
        break
    else:
        toppings.append(topping)
print("Your pizza has the following toppings:")
for topping in toppings:
    print(f"- {topping}")
print("Thank you for using our pizza topping service!")