
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
print('\n')

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
print('\n')

print('pasta' in food)
print('orange' in food)

# Nested lists

numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']
combined = [numbers, letters]
print(combined[0][1], combined[1][1])

# Lists can have multiple data types

my_list = ['red', 5, ['green', 'apple', 'blue'], 10]
print('\n')

print(my_list)
print(my_list[2][0])
print(my_list[0])

# list methods

# append

my_fruits = ["apple"]
my_fruits.append("pear")
print('\n')

print(my_fruits)

# Remove

my_fruits.remove("apple")
print('\n')
print(my_fruits)

# Insert

my_fruits.insert(0, 'mango')
my_fruits.insert(1, 'melon')
print('\n')
print(my_fruits)

# Extend with a list

my_fruits.extend(['grape', 'cherry'])
print('\n')
print(my_fruits)

# Find index 

print('\n')
print(my_fruits.index('grape'))

# Reverse

my_fruits.reverse()
print('\n')
print(my_fruits)

# Sort

my_fruits.sort()
print('\n')
print(my_fruits)

my_fruits.sort(key=len)
print('\n')
print(my_fruits)

# Join

x = ", ".join(my_fruits)
print('\n')
print(x)

# Dictionaries - defined {}

'''
Similar to list but no index
Keys have to be unique, values dont
'''

drinks = {'fizzy': 'sprite', 'still': 'water', 'juice': 'orange', 'alcoholic': 'beer'}
print('\n')
print(drinks)
print(drinks['still'])

# Overwrite

drinks['non-alcoholic'] = 'squash'
print('\n')
print(drinks)

# Return all keys or values
print('\n')

print(drinks.values())
print(drinks.keys())
print(drinks.items())

print('\n')

print("water" in drinks.values())
print('still' in drinks)

# Update
print('\n')

drinks.update({'sugary': 'cola'})
print(drinks)
# Or
drinks.update(very_sugary = 'red-bull')
print(drinks)

# Pop
print('\n')

print(drinks.pop("non-alcoholic"))
print(drinks)
print(drinks.pop("non-alcoholic", 'not found'))

# Tuples 
# We cant change data in a tuple
# () instead of [] or use nothing at all

shapes = ('square', 'circle', 'triangle')
shapes1 = 'square', 'circle', 'hexagon'
print('\n')

print(type(shapes))
print(type(shapes1))

print('\n')
# shapes.append('rectangle')
print(shapes)

'''
Makes it clear we dont want the values to change
Less memory to store data
Speed - Tuples are quicker than lists - its very minimal
'''

'''
Sets
Unordered - no indexing
no duplicate values
cant be nested
{}
'''

items = {'apple', 'banana', 'pear'}
print('\n')
print(type(items))

# Dictionary exercise

books = {"The handmaiden's Tale": "Margaret Atwood", "The Hobbit": "Tolkien", "Charlie and the chocolate factory": "Roald Dahl" }
print('\n')
print(books["The handmaiden's Tale"])

books_dict = {"Author1": ["Book1", "Book2"], "Author2": ["Book3", "Book4"]}

y = input("Enter author name: ")
print(", ".join(books_dict[y]))
