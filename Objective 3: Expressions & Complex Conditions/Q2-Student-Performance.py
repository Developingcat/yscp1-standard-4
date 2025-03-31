'''
Question 2: Student Performance
Description: Write a program that checks if a student has passed or failed based on two conditions:

The student's grade must be 65 or higher.
The student must have attended more than 75% of the classes.
'''

# This program checks if a student passes based on grade and attendance

grade = float(input("Enter your grade: "))
attendance = float(input("Enter your attendance percentage: "))

# Use complex conditions to determine if the student passed

if grade >= 90:
    print("Your grade passed!") 
elif grade >= 80: 
    print("Your grade passed!")
elif grade >= 70:
    print("Your grade passed!")
elif grade >= 60:
    print("Just barely.")
else: 
    print("Better luck next year.")

if attendance >= 75:
    print("You pass!! Congratulations!!")
else: 
    print("But your attendance says otherwiswe, better luck next year!")