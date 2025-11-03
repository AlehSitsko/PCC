# Sandwiches
def make_sandwich(*ingredients):
    """ Print the list of ingredients that have been requested for the sandwich. """
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
# Call the function with different numbers of ingredients
make_sandwich("ham", "cheese", "lettuce", "tomato")
make_sandwich("turkey", "avocado", "mayo")
make_sandwich("peanut butter", "jelly")