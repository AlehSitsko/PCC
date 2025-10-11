# Calculate daily sales for a pizza store
# Sales examples
orders = [
    {"id": 1, "item": "Pizza", "price": 12.5, "quantity": 2},
    {"id": 2, "item": "Burger", "price": 8.0, "quantity": 3},
    {"id": 3, "item": "Cola", "price": 2.5, "quantity": 5}
]
# Function to calculate total sales and show most popular and most valuable item
def calculate_summ(order_list):
    total = 0
    item_counts = {}
    item_values = {}
    for order in order_list:
        price = order.get("price", 0)
        quantity = order.get("quantity", 0)
        total += price * quantity
        item = order.get("item")
        if item:
            item_values[item] = item_values.get(item, 0) + price * quantity
        if item:
            item_counts[item] = item_counts.get(item, 0) + quantity
    if item_counts:
        most_popular = max(item_counts, key=item_counts.get)
        print(f"Most popular item: {most_popular} (sold {item_counts[most_popular]} units)")
    if item_values:
        most_valuable = max(item_values, key=item_values.get)
        print(f"Most valuable item: {most_valuable} (total sales ${item_values[most_valuable]:.2f})")
    return total
# Example usage
if __name__ == "__main__":
    total_sales = calculate_summ(orders)
    print(f"Total sales for the day: ${total_sales:.2f}")