# program to go to a specific date
from  datetime import datetime
from dateutil import relativedelta

today = datetime.now()


print('---- Get to the first day of thr month -----')

first_day = today + relativedelta.relativedelta(day = 1) # 17-12-2023
print(first_day)

print('---- Get to the last day of the month ------')
last_day = today + relativedelta.relativedelta(day = 31)# 31-12-2023
print(last_day)

