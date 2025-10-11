# Dictionary with cities, their country, population, and fact
cities = {
    'New York': {
        'country': 'USA',
        'population': 8419600,
        'fact': 'The Big Apple',
    },
    'Los Angeles': {
        'country': 'USA',
        'population': 3980400,
        'fact': 'City of Angels',
    },
    'Chicago': {
        'country': 'USA',
        'population': 2716000,
        'fact': 'The Windy City',
    },
}
# Looping through the cities dictionary and printing information about each city
for city, info in cities.items():
    country = info['country']
    population = info['population']
    fact = info['fact']
    print(f"{city} is in {country}, has a population of {population}, and is known as '{fact}'.")