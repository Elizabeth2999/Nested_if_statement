year = int(input("what year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('This is a leap year because it is evenly divided by 4, 100 and 400')
        else:
            print('This is not a leap year because it is not evenly divided by 400, even though it is evenly divided '
                  'by 4 and 100')

    else:
        print("This is a leap year because it is not evenly divided by 100, but it is evenly divided by 4 ")
else:
    print('This is not a leap year because it is not evenly divisible by 4')

