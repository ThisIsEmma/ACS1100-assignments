# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the descirption. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!


print("Welcome to the simple interest calculator! \n\nThis calculator will calculate the final amount (A) one would get after investing a sum of money (P) for a certain period of time (t) at a given rate (r). \n\nThe compound interest formula is A = P(1 + rt)")

#Formula used for simple interest calculator is available at https://www.calculatorsoup.com/calculators/financial/simple-interest-plus-principal-calculator.php 

def simple_interest_cal(principal, time, rate):
    final_amount = principal * (1 + (rate * time))
    return final_amount

#1 - Gather user input

principal = input("Please enter the amount you wish to invest: ")
time = input("For how many years will you invest it: ")
str_principal_currency = input("Please specify currency (i.e $, €, etc.)")
rate = input("At what interest rate (in percentage, for example 3 or 5): ")

#2 - Convert collected data into appropriate data type and complete the calc

float_principal = float(principal)
float_time = float(time)
float_rate = (float(rate))/100

final_amount = simple_interest_cal(float_principal, float_time, float_rate)

#3 - Print the result 

print(f"If you invest {str_principal_currency}{principal} today, at {rate}% interest rate during a period of {time} year(s), you will end up with {str_principal_currency}{final_amount}")
