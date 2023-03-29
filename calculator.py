
# Define the function for the calculator
def calculator():
    # Get the input from the user
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
 
    # Perform the calculation based on the operator input
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print("Invalid operator")
 
    # Display the result to the user
    print("The result is", result)
 
# Call the calculator function
calculator()