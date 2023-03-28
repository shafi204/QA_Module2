
grade = int(input("Enter your exam mark: "))

while grade >100 or grade <1:
    print("You have entered an invalid mark. Try again: ")
    break

if grade <50:
    print("You have failed the exam")
elif grade >= 50 and grade <=60:
    print("You have passed")
elif grade >=61 and grade <70:
    print("You have achieved a merit")
elif grade >=71 and grade <=100:
    print("Congratulations you have achieved a distinction!")
    

