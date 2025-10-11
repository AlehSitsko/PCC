# Deli
sandwich_orders = ["tuna", "ham", "turkey", "pastrami"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Making {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("All sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")