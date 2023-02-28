# Using my summing a million program for slicing.
million = list(range(1, 1000001))
print("The minimum number in my list is:")
print(min(million))
print("The maximum number in my list is:")
print(max(million))
print("The sum of my entire list is:")
print(sum(million))
print("The first 3 numbers in my list are:")
for num in million[:3]:
    print(num)
print("The three numbers in the middle of my list are:")
for num in million[499999:500002]:
    print(num)
print("The last 3 numbers in my list are:")
for num in million[999997:]:
    print(num)