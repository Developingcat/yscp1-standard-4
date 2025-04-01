'''
Question 3: Tax Calculation
Description: Write a program that calculates the tax on a purchase based on the price. 
The tax rate should be 8% if the price is under $100 and 10% if it’s $100 or more.
'''

# This program calculates the tax based on price

price = float(input("Enter the price of the item: $ "))


# Study for Pt. The Triality 
# Use complex conditions to calculate the tax rate

# Okay so first focus on the prices and such, 8% is going to be a decimal since it's 8/100, move it two places over 
# So the number percents: 0.008 and 0.001 for the percents 


# And then evil plug in time 

# All those tax caluclators and I forgot the formula for these  

# I still can't format my decimals right :( I swear it was :.2f after the variable but I keep getting an error for an 
# invalid decimal literal and I do not know how to fix it 

if price >= 100:
    totalPrice = price * 10 / 100
    totalDoublePrice = price + totalPrice
    print(f"Your total is: ", totalDoublePrice) 
elif price <= 100: 
    totalSecond = price * 8 / 100
    totalCost = price + totalSecond 
    print(f"Your total is: ", totalCost)  
else: 
    print("Please do not bully my code......")

# if price <= 100:
#     final_calc = price * 0.8
#     print(f"Your final price should be:", final_calc)
# else: 
#     final_calc = price * 00.1
#     print(f"Your final price should be:",final_calc)