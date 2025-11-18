# Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
# Example usage task 9-1
# 1st restaurant
my_restaurant = Restaurant("Pasta Palace", "Italian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# 2nd restaurant
another_restaurant = Restaurant("Sushi World", "Japanese")
another_restaurant.describe_restaurant()
another_restaurant.open_restaurant()

# 3rd restaurant for task 9-2
third_restaurant = Restaurant("Taco Town", "Mexican")
third_restaurant.describe_restaurant()
third_restaurant.open_restaurant()
