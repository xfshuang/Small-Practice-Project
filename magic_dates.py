#Name: Shirley Huang
#Date: 12/15/2019

month = int(input('Enter the number for a month: '))
day = int(input('Enter the number for a day: '))
year = int(input('Enter a two-digit year: '))
if (month*day) == year:
    print('That date is magic!')
else:
    print("Sorry, that's just a regular date... not magic.")
