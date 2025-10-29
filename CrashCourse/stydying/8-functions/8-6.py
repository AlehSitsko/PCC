# City names
def city_country(city, country):
    """Return a formatted string of city and country."""
    return f'"{city.title()}, {country.title()}"'
# Function to print city-country pairs
def print_city_country(city, country):
    """Print a formatted string of city and country."""
    print(city_country(city, country))
# Calling the functions with different city-country pairs
print_city_country("santiago", "chile")
print_city_country("madrid", "spain")
print_city_country("tokyo", "japan")