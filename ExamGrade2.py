
#grade = int(input("Please enter your exam mark: "))

def grade():
    marks = int(input("Please enter your marks: "))
    if marks < 1 or marks > 100:
        print("Invalid input. Exam mark must be between 1 and 100. Please try again")
    level = int(input("Please enter your level: "))

    while level == '1':
        if marks < 50:
            print("You have failed the exam")
        elif marks >= 50 and marks <= 60:
            print("You have passed the exam")
        elif marks >= 61 and marks <= 70:
            print("You have earned a merit for the exam")
        elif marks >= 71 and marks <= 100:
            print("You have earned a distinction for the exam")
    grade()   
    
grade()

   