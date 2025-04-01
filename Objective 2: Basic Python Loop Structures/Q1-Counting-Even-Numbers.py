'''
Question 1: Counting Even Numbers

Description: Write a program that counts how many even numbers there are in a list of numbers (from 1 to 20).
'''

# This program will count even numbers in a list

# Maybe make this a variable of some flavor to contain it all? The For Loop won't run it and I have never seen it with 
# My eyes before

numbers = list(range(1, 21))
even_count = 0 

numbersList = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 ]

# It may be a bit overcomplicated but it works!! YAHOOO!!! 
# Loop through the numbers and check for even numbers

for i in range(1,21):
    resultsOne = i % 2 
    print(i)
    if resultsOne == 0: 
        print("Even!! Yahooie!! ") 
    else: 
        print("Not an even number.... darn")