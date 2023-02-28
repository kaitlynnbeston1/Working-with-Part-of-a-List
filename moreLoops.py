my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
# the loops; using list comprehention
print("My favorite foods are:")
[print(food) for food in my_foods]
print("\nMy friend's favorite foods are:")
[print(food) for food in friend_foods]