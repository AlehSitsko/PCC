# foods.py
# foods list
my_foods = ['pizza', 'falafel', 'carrot cake']
# copy of the foods list
friend_foods = my_foods[:]

# add different food to the end of the list
friend_foods.append('ice cream')

# print my fav food
for food in my_foods:
    print(f"I like {food}.")

# print friend's fav food
for food in friend_foods:
    print(f"My friend likes {food}.")