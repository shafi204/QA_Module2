
num1 = int(input("Please enter a number: "))
num2 = float(input("Please enter another number: "))

print("1.", "Add", "\t\t", "+" )
print("2.", "Subtract", "\t", '-' )
print("3.", "Mutiply", '\t', '*')
print('4.', 'Divide', '\t', '/')
print('5.', 'Square', '\t', 's')

operator = input("Please select an operator from the list above: ")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print("Invalid operator please try again")

print(result)
