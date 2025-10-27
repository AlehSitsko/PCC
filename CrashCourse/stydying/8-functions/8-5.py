# Cities 
def describe_city(city, country="Iceland"):
    """Display information about a city and its country."""
    print(f"{city.title()} is in {country.title()}.")

# Calling the function with different cities
describe_city("Reykjavik")
describe_city("Paris", "France")