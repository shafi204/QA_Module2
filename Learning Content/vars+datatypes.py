# Variables - A reference - The name of a variable
# - A section of memory

# Naming convention: Name should be descriptive, start with lowercase and not a number

''' 
x = '5'
var = 5
my_var_is_easy_to_read
myVarIsEasyToReady
'''

'''
print = 5  # Dont use reserved words
1var = 5   # Dont start with a number
Var = 5   # Dont start with a capital
VAR = 5   # Not in caps
'''

print('x')

# print() data displayed to standard output
# input() user inputted text from standard input, string by default
# type() the data type of a variable

name = input("name: ")
print("Your name is" + " " + name)
print("Your name is", name)
print(f"Your name is {name}")
print(type(name))

age = input('What is your age: ')
age1 = int(input('What is your age: '))

print(type(age))
print(type(age1))

'''
Four main data types in Python:
String: plain text, used to display info. Word, sentence, paragraph, str means string
Integers: A whole number
Float: A decimal number
Boolean: True or False. Case sensitive. Equivalent to 0 and 1
'''

first_name = 'Steve'
age = 32
# Float 
wallet = 29.99

name = 'Rex'
age = 3
bark = True
meow = False

'''Escape characters
\\ backslash, \n newline, \t tab, u\ or U\ unicode or extended unicode
'''

print("Person 1: \tHey, how are you? \nPerson2: \tGood thanks! \U0001F604")

print("Hello World".lower())
print("Hello World".upper())
print("Hello World".replace("World", "class"))
print("hello world".split())
print('Hello world'.count('1'))


