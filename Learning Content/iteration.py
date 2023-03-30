
# Iteration is another word for loops, repeating a block of code over and over 
# We do not have to write the code multiple times which in turn saves time

'''
There are two types of loops
While loops
For loops
'''

# While loops
'''
A while loop will continue to execute code while a condition is true
If the condition is never true the while loop will never start
'''

print('1')
print('2')
print('3')

x = 0

while x < 100:
    print(x)
    x += 1  # Same as x = x + 1

# break

print('\n')

i = 1

while i < 6:
    if i == 3:
        break
    print(i)
    i += 1

# continue

print('\n')

j = 0

while j < 6:
    j += 1 
    if j == 3:
        continue
    print(j)

print('\n')

k = 1 

while k < 6:
    print(k)
    k += 1
else:
    print("k is no longer less than 6")


# For loops
'''
A for loop will iterate over any iterable collection - lists/strings/dictionaries
Useful for when we want to use data in a collection
Do something to individual elements in a collection
'''

# Iterating through lists
print('\n')

numbers = [1, 3, 5, 9]
for item in numbers:
    print(item)

# Using a while loop 

print('\n')

l = 0
while l < len(numbers):
    print(numbers[l])
    l += 1

# Change items

my_fruits = ['apple', 'orange', 'banana']
print('\n')
for fruits in my_fruits:
    print(fruits.upper())

# Range function
print('\n')

for a in range(5):
    print(a)    # 0-4 (stops at 5)

for a in range(1,5):
    print(a)    # 1-4

for a in range(1,10,2):
    print(a)    # 1 to 9 in increments of 2

# Strings
print('\n')

for x in 'hello':
    print(x)

print('\n')

for word in 'hello world'.split():
    print(word)

# List comprehensions
print('\n')

results = [x**2 for x in range(5)]
print(results)

# Same as

results = []
for x in range(5):
    results.append(x**2)
print(results)

# Dictionary iterations
print('\n')

for i in {'drink': 'wine'}:
    print(i)

for value in {'food': 'jam'}.values():
    print(value)

for key, value in {'shape': 'square'}.items():
    print(key, value)

# break and continue
print('\n')

for i in range(10):
    print(i)
    if i == 5:
        break

# Nested loops
print('\n')

for i in range(3):
    for j in range(4):
        print(i, 'x', j, '=', i*j)
        
# Write a while loop which asks for the names of 5 people, for each person print their name followed by text 'is great!'
print('\n')

counter = 0

while counter < 5:
    name = input("Please enter your name: ")
    print(name + ' is great!')
    counter +=1