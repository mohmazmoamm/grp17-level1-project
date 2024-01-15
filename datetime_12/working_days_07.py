# Write a program to GEt the date after 12 Working days from a date
from datetime import datetime
from dateutil import relativedelta

today = datetime.now()
required_date = today
jump_days = 12

# start date = 25-12-2023      end date : 10-1-2023
for i in range(jump_days):
    if today.date().weekday() == 3:
       required_date= required_date + relativedelta.relativedelta(days = 3)
    elif today.date().weekday() == 4:
        required_date = required_date + relativedelta.relativedelta(days = 4)
    else:
       required_date = required_date + relativedelta.relativedelta(days = 1)


print(f' After {jump_days} working days from {today.date()}, the new date is {required_date.date()}')



