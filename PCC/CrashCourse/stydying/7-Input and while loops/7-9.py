# No Pastrami
sandwich_orders = ["tuna", "ham", "turkey", "pastrami"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    if current_sandwich == "pastrami":
        print("Sorry, we're out of pastrami.")
        continue
    print(f"Making {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("All sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")