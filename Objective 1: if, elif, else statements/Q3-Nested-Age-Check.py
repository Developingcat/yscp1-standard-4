'''
Question 3: Nested Age Check
Description: Write a program that checks a persons age and prints a message. The program should have the following logic:

If the person is below 13, print "Child".
If the person is between 13 and 19, print "Teenager".
If the person is between 20 and 64, print "Adult".
If the person is 65 or older, print "Senior".
If the persons age is 18 or 21, print "Young Adult".

The last one and the second one blatantly overwrite one another..... erm......
'''

# This program will check age categories

age = int(input("Enter your age: "))

# Add if-elif-else logic here with nested conditions


# Unfortunately, I get the feeling of and statements, and it saddens me 

# and age > 18

if age <= 13: 
    print("Child")
# elif age <= 18 or age <= 21: 
#     print("Young Adult")
elif age <= 13 or age < 18:
    print("Teenager.")
elif age <= 19 or age <= 21: 
    print("Young Adult")
elif age >= 21 and age < 65: 
    print("Adult")
elif age >= 65:
    print("Senior")
else: 
    print("Huh.") 
