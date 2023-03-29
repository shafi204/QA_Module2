
print("Pythagoras' Calculator")
print("1.", " ", 'Find the length of A given B and C')
print("2.", " ", 'Find the length of B given A and C')
print("3.", " ", 'Find the length of C given A and B')

print('\n')
num1 = int(input("Please enter an option from the list above: "))

if num1 == 1:
    side_b = float(input("Eneter length of side B: "))
    side_c = float(input("Eneter length of side C: "))
    side_a = (side_c**2 - side_b**2) **0.5
    print("Length of side A is: ", side_a)

elif num1 == 2:
    side_a = float(input("Eneter length of side A: "))
    side_c = float(input("Eneter length of side C: "))
    side_b = (side_c**2 - side_a**2) **0.5
    print("Length of side B is: ", side_b) 

elif num1 == 3:
    side_a = float(input("Eneter length of side A: "))
    side_b = float(input("Eneter length of side B: "))
    side_c = (side_a**2 + side_b**2) **0.5
    print("Length of side C is: ", side_c)

else:
    print("Invalid input. Please try again")



