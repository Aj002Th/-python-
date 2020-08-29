year = input('consult if the year you think is leap year:')
if year.isdigit():
    i = int(year)
    if (i % 4 ==0 and i % 100 != 0) or i % 400 ==0:
        print("yes," + year +" is a leap year!")
    else:
        print("no," + year +" isn't a leap year!")
else:
    print('what you input is not a year!')
