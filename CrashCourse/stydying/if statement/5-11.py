# Ordinal numbers
# List of numbers 1 to 9
numbers = list(range(1, 10))
# Loop through the numbers and print their ordinal representation
for number in numbers:
    if number == 1:
        suffix = 'st'
    elif number == 2:
        suffix = 'nd'
    elif number == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    print(f"{number}{suffix}")