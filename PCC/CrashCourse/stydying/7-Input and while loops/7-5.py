# Movie tickets
while True:
    age = input("Enter your age (enter 'quit' to end): ")
    if age.lower() == 'quit':
        break
    age = int(age)
    if age <= 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    elif age <= 12:
        print("Your ticket costs $12.")
    else:
        print("Your ticket costs $15.")