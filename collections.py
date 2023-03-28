
# There are different ways to store data 
'''
Lists - ordered, mutable, collection of values
Dictionaries - unordered, mutable, collection of key-value pairs
Tuple - ordered, immutable, collection of values
Sets - unordered, mutable, collection of unique values
'''

# Mutable can be changed. Immutable cannot be changed

# Lists - Multiple values contained in a single variable, defined by square brackets with commas. [,]

colours = ['red', 'blue', 'green', 'yellow', 'orange', 'white', 'black']
print(colours)

# Referencing - Elements in a list are referenced by their position (or index). This starts from position 0
#               Backwards would be -1

print(colours[0])
print(colours[-4])

# sub-list of items by slicing, including first number, excluding the last

print(colours[0:2])
print(colours[1:])

# Altering lists using index and new value, delete with del keyword

food = ['bread', 'cheese', 'pasta', 'apple', 'fries', 'banana']
food[0] = 'rice'
del food[1]
print(food)

# Checking if item is still in the list

print('pasta' in food)
print('orange' in food)

# Nested lists

numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']
combined = [numbers, letters]
print(combined[0][1], combined[1][1])

# Lists can have multiple data types

my_list = ['red', 5, ['green', 'apple', 'blue'], 10]
print(my_list)
print(my_list[2][0])
print(my_list[0])

# list methods

# append

my_fruits = ["apple"]