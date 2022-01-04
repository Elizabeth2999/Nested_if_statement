print('Welcome to the tip calculator!')

Total_bill = float(input('What was the total bill? $'))
tip = int(input('How much tip would you like to give in percentage? 10, 12, or 15: '))
no_of_people = int(input('How many people are to split the bill? '))

total_bill_tip = ((tip/100) * Total_bill) + Total_bill
bill_per_person = round((total_bill_tip/no_of_people), 2)

print(f'the bill per person is ${bill_per_person}, thank you for your patronage!')