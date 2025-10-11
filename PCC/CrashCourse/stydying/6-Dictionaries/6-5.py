# 6-5 Rivers
# Dictionary with some major rivers and the countries they flow through
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
    'mississippi': 'united states',
    'danube': 'multiple countries in europe',
}
# Printing each river and the country it flows through
for river, country in rivers.items():
    print(f"The {river.title()} River flows through {country.title()}.")
# Printing lists of rivers 
print("\nList of rivers:")
for river in rivers.keys():
    print(f"- {river.title()}")
# Printing list of countries
print("\nList of countries:")
for country in set(rivers.values()):
    print(f"- {country.title()}")