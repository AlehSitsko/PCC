# taks 9-4
# attrubute for number of served customers
    
# Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional_customers):
        self.number_served += additional_customers

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        print(f"Number of Customers Served: {self.number_served}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
# Example usage task 9-1
# 1st restaurant
my_restaurant = Restaurant("Pasta Palace", "Italian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(25)
my_restaurant.increment_number_served(10)

# 2nd restaurant
another_restaurant = Restaurant("Sushi World", "Japanese")
another_restaurant.describe_restaurant()
another_restaurant.open_restaurant()
another_restaurant.set_number_served(40)
another_restaurant.increment_number_served(15)

# 3rd restaurant for task 9-2
third_restaurant = Restaurant("Taco Town", "Mexican")
third_restaurant.describe_restaurant()
third_restaurant.open_restaurant()
third_restaurant.set_number_served(30)
third_restaurant.increment_number_served(20)
# Display updated number of served customers
print("\nUpdated Customer Counts:")
my_restaurant.describe_restaurant()
another_restaurant.describe_restaurant()
third_restaurant.describe_restaurant()