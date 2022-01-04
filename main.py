print('Welcome to the tip calculator!')
Total_bill =input('What was the total bill? ')
tip = input('How much tip would you like to give in percentage? 10, 12, or 15:  ')
no_of_people = input('How many people are to split the bill? ')
percentage_tip = (int(tip)/100 * float(Total_bill))
bill = round( ((float(Total_bill)/int(no_of_people) +(percentage_tip/5))), 2)

print(f'the bill per person is {bill}, thank you for your patronage!')
