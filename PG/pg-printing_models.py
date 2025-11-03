# List of models for printing
unprinted_models = [
    "product.template",
    "sale.order",
    "account.invoice",
    "stock.picking",
]
# Empty list for adding printed models
printed_models = []
# Function to print models
def print_models():
    """Simulate printing each model, until none are left."""
    while unprinted_models:
        current_model = unprinted_models.pop()
        print(f"Printing model: {current_model}")
        printed_models.append(current_model)
# Print printed models
print("Printed models:")
for model in printed_models:
    print(f"- {model}")

# Call the function to print models
print_models()
# Print printed models after printing
print("Printed models after printing:")
for model in printed_models:
    print(f"- {model}")