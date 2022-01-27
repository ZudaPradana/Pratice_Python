# tip calculator
total_bill = float(input('What was the total bill? $'))
percetage_tip = int(input('What percentage tip would you like to give?'))
split_bill = int(input('How many people to split the bill? '))
convert_percentage = percetage_tip / 100
convert_bill = round(convert_percentage * total_bill, 2)
calc_pays = round((convert_bill + total_bill) / split_bill,2)
print(f'Total bill: ${total_bill+convert_bill}')
print(f'Each person should pay: ${calc_pays}')


# CHALLANGE
# random pay the bills
split = makes string to list
import random
name = input('input the name who you want to pay the bills :  \n')
split = name.split()
print(f'{random.choice(split)} need to pay the bils')
