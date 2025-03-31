'''
Question 3: Tax Calculation
Description: Write a program that calculates the tax on a purchase based on the price. 
The tax rate should be 8% if the price is under $100 and 10% if it’s $100 or more.
'''

# This program calculates the tax based on price

price = float(input("Enter the price of the item: $ "))


# Study for Pt. The Triality 
# Use complex conditions to calculate the tax rate

if price <= 100:
    final_calc = price * 8/100
    print(f"Your final price should be:", final_calc)
else: 
    final_calc = price * 10/100 
    print(f"Your final price should be:",final_calc)