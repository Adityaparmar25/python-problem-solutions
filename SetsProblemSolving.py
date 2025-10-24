# write a program to find max and min in a set.
a = {41,56,52,6,9,5,56,9}
maximum = max(a)
minimum = min(a)
print("The minimum Value in the set is",minimum)
print("The maximum Value in the set is",maximum)

# Write a program to find common elements in three lists using sets
a = [1,5,9,6,4,7]
b = [5,4,9,6,0]
c = [1,6,7,5,2]

print(set(a) & set(b) & set(c))

# Write a program to find difference between two sets
a = {1, 5, 9, 6, 4, 7}
b = {5, 4, 9, 6, 0}

print(a.difference(b))

# Write a python program to remove an item from a set if it present in the set
a = {1, 5, 9, 6, 4, 7}
a.discard(7)
print(a)

# Write a python program to check if a set is a subset of another set
a = {1, 5, 9, 6, 4, 7}
b = {5, 4, 9, 6, }

print(b.issubset(a))