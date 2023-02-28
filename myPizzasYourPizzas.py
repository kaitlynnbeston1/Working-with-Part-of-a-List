myPizzas = ["vegetarian", "cheese", "ham and pineapple"]
friendPizzas = myPizzas[:]
myPizzas.append("spinach and feta")
friendPizzas.append("all dressed")
print("My favorite pizzas are:")
[print(pizza) for pizza in myPizzas]
print("My friend's favorite pizzas are:")
[print(pizza) for pizza in friendPizzas]