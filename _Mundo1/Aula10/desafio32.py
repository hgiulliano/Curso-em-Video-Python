from datetime import date
year = int(input('In wich year you are using this program? (if you want to use the actual year write 0): '))
if year == 0:
    year = date.today().year
if (year%4) == 0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is a normal year')