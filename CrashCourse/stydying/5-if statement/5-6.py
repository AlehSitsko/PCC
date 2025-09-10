#Stages of life
ages = [2, 4, 13, 20, 65, 70]
# Evaluate each age and print the corresponding stage of life
for age in ages:
    if age  < 2:
        print(f"Age {age}: This person is a baby.")
    elif age >= 2 and age < 4:
        print(f"Age {age}: This person is a toddler.")
    elif age >= 4 and age < 13:
        print(f"Age {age}: This person is a kid.")
    elif age >= 13 and age < 20:
        print(f"Age {age}: This person is a teenager.")
    elif age >= 20 and age < 65:
        print(f"Age {age}: This person is an adult.")
    elif age >= 65:
        print(f"Age {age}: This person is a senior citizen.")
