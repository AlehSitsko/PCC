# Funcrion that calculates price of items in a shopping cart
#Dictionary of items and their prices
item_prices = {
    "apple": 0.99,
    "banana": 0.59,
    "milk": 2.49,
    "bread": 1.99,
    "eggs": 2.99
}

# Function to calculate total price
def calculate_total(cart):
    total = 0
    for item in cart:
        price = item_prices.get(item, 0)
        total += price
    return total
# Example usage
if __name__ == "__main__":
    shopping_cart = ["apple", "banana", "milk", "bread", "eggs"]
    total_price = calculate_total(shopping_cart)
    print(f"Total price of items in the cart: ${total_price:.2f}")