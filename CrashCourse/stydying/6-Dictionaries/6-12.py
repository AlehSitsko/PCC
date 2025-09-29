# Dictionaries with world wonders
world_wonders = {
    'Great Wall of China': {
        'location': 'China',
        'year_completed': '1644',
        'fact': 'The longest wall in the world.',
    },
    'Machu Picchu': {
        'location': 'Peru',
        'year_completed': '1450',
        'fact': 'An ancient Incan city located in the Andes mountains.',
    },
    'Christ the Redeemer': {
        'location': 'Brazil',
        'year_completed': '1931',
        'fact': 'A giant statue of Jesus Christ overlooking Rio de Janeiro.',
    },
}
# Looping through the world_wonders dictionary and formatted printing information about each wonder
for wonder, info in world_wonders.items():
    location = info['location']
    year_completed = info['year_completed']
    fact = info['fact']
    print(f"{wonder} is located in {location}, was completed in {year_completed}, and is known for: {fact}")