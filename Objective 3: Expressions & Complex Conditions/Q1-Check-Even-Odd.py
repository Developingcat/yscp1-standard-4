'''
Question 1: Check for Even or Odd
Description: Write a program that takes an integer as input and 
checks if it's even or odd using a combination of relational and logical operators.
'''

# This program will check if the input number is even or odd

number = int(input("Enter a number: "))

# Use relational and logical operators to check for even/odd & Print out which it is to the terminal

if number % 2 == 0: 
    print("This number is even!")
else: 
    print("This number is not even.")