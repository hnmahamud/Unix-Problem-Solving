from datetime import date

def ageCal(current_date, current_month, current_year, birth_date, birth_month, birth_year, leap):
    if leap == True:
        month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (birth_date > current_date):
        current_month = current_month - 1
        current_date = current_date + month[birth_month - 1]

    if (birth_month > current_month):
        current_year = current_year - 1
        current_month = current_month + 12

    calculated_date = current_date - birth_date
    calculated_month = current_month - birth_month
    calculated_year = current_year - birth_year
    calculated_week = int(calculated_date / 7)
    calculated_days = calculated_date - (calculated_week * 7)

    print()

    print('Age:')
    print(calculated_year, "years" + ",", calculated_month, "months" + ",", calculated_week, "weeks" + ",", calculated_days, "days" + " have passed")
    
    print()


today = date.today()
current_date = today.day
current_month = today.month
current_year = today.year

date_entry = input('Enter Birth date (i.e. 2020,01,01): ')
year, month, day = map(int, date_entry.split(','))
birth_date = day
birth_month = month
birth_year = year

if birth_year % 4 == 0 and birth_year % 100 != 0:
    leap = True
    ageCal(current_date, current_month, current_year, birth_date, birth_month, birth_year, leap)
    print(birth_year, "is a Leap Year")
elif birth_year % 100 == 0:
    leap = False
    ageCal(current_date, current_month, current_year, birth_date, birth_month, birth_year, leap)
    print(birth_year, "is not a Leap Year")
elif birth_year % 400 == 0:
    leap = True
    ageCal(current_date, current_month, current_year, birth_date, birth_month, birth_year, leap)
    print(birth_year, "is a Leap Year")
else:
    leap = False
    ageCal(current_date, current_month, current_year, birth_date, birth_month, birth_year, leap)
    print(birth_year, "is not a Leap Year")