# here we will show all basic operations on datetime
from datetime import datetime  # from module import class datetime



print('------ Set the current date and time -----')
today = datetime.now()
print(today)
print('----- Get only date or time or their parts------')
print(today.date())
print(today.date().month)
print(today.date().day)

print(today.time())
print(today.time().hour)
print(today.time().minute)
print(today.time().second)

print('-------- Re Formating date,  time --- | we use strftime() function------')
print('----- Convert data into string using strftime() function-----')

print(today.strftime(' %d-%m-%Y %y %w $M'),) # day, month, year, yr, weekday
print(today.strftime('%B-%b-%A-%a')) # Month, Mon, Day, Dy
print(today.strftime('%H-%M-%S')) # Hours in 24 Style
print(today.strftime('%I-%M-%S-%p'))
print(today.strftime('%H-%M-%S'))

print('---------------------- Create a Custom date : 24-04-2023')
print('--- 1st way : datetime object using constructor () ')
# custom_date = datetimr(year=2023, month=4, day-24)
custom_date = datetime(2023, 12, 25)
print(custom_date)

print('---- 2nd way - by Converting a string to Data using strftime.() function----')
date_style_string = '24-4-2023'
new_custom_date = datetime.strptime(date_style_string,  '%d-%m-%Y')
print(new_custom_date)

print('------------------ Comparison ---------------')
if today.date() > custom_date.date():
    print('Today is newer than custom date')
elif today.date() < custom_date.date():
    print('Today is older than custom date')
else:
    print('2 dates are equal')
