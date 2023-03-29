# if, elif, else
'''
Conditional statements are used to accomadate different paths our code might take
We use if statements to run code if a given condition is met
'''

my_bool = False
if my_bool:
    print("My bool is True")
else:
    print("My bool is false")

# We can nest if statements 

# if some condition:
#    if some other condition    
#           .....
#    else:
#           .....
# else:
#   .....

#Conditionals
'''
Equals to - ==
Not equal to - !=
Less than - <
More than - >
Less than or equal to - <= / >=
'''
print('\n')
money = 1

if money > 10:
    print("I have some money")
else:
    print("I dont have much")

# Elif - Else if
'''
We dont always need to check if every statement evaluates to true
Mostly only one statement will be true
Elif makes our code more efficient 
Will only run if no other statement has been evaluated as true
'''

temp = 5

if temp >= 30:
    print("Its a very hot day")
elif temp > 25:
    print("Its a hot day")
elif temp > 20:
    print("Its okay")
elif temp > 15:
    print("It could be better")
elif temp == 0:
    print("Its exactly freezing")
else:
    print("Its cold")

# Exercise

'''
Ask for an input form a user for a grade/mark
If the mark is greater than 85 print 'distinction'
If the mark is between 65 and 85 print 'pass'
Anything else print 'fail'
'''

print('\n')
x = int(input("Enter a grade: "))

if x >= 85:
    print("You have achieved a distinction")
elif x >= 65:
    print("You have passed")
else:
    print("You have failed")


# Multiple comparators + with multiple conditions using and/or:

deposit = 10 
password = 'passwordd1234'
print('\n')

if 0 < deposit <= 100 and password == 'password':
    print(f'Thank you for £{deposit} deposit!')
else:
    print("Failed to deposit")

# Not 

print('\n')

deposit = 0
password = 'password'

if not (0 < deposit <= 100) or password != 'password':
    print("Failed to deposit")
else:
    print(f'Thank you for £{deposit} deposit!')

# In and not in

name = 'root'
print('\n')

if name in ('root', 'admin'):
    print("This is not a valid username")
else:
    print(f'Welcome {name}')

# Challenge    
'''
Weight converter app, convert a user inputted weight (float) and user to select either kgs or lbs
from a promt. Write an if statement that checks if the unit entered is kgs or lbs. If kgs convert into
lbs and print converted weight
'''

# Error handling - User should be able to enter lowercase or uppercase
print('\n')

weight = float(input("Enter your weight: "))
unit = input("K (kgs) or L for (lbs): ")
if unit.upper() == 'K':
    converted = weight / 0.45
    print("Weight in Lbs: ", converted)
else:
    converted = weight * 0.45
    print("Weight in Kgs: ", converted)