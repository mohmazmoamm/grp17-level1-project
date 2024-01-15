# show all printing options

emp_id = 101
emp_name = 'Esam Omar'
emp_salary = 7853.6782123
print('------- 1. print with concat ---------')
print(' emp has id = '+ str(emp_id) +', his name is '+emp_name+',\ntakes salary = '+str(emp_salary))

print('----------2, print with multi paramters ------------')
print(' Emp has id = ', emp_id, ', his name is ', emp_name, ', takes salary = ', emp_salary)
print(150, 120, 200, 30, sep= '-')
for i in range(1, 11):
    print(i, end=' ')

print('\ntest')
print('test2')

print('--------- 3, String formatting using placeholders ------- is id if ----')
print('Emp has id = %d, his name is %s, takes salary = %f' %(emp_id,  emp_name, emp_salary))

print('--------- 4, string formatting using functions -------------')
print('Emp has id = {}, his name is {}, takes salary = {:,.2f}'. format(emp_id, emp_name, emp_salary))

print('-----5, string formatting using F-string function ---------')
print('F ' 'Emp has id = {emp_id}, his name is {emp_name}, takes salary = {emp_salary:,.2f}')

# ------------- numbers functions accuracy : round, math.trunc, math.ceil, math.floor

emp_salary = 78954.6782123
print('F''using ceil function, result = {round(emp_salary, 2)}')
print('F''using ceil function, result = {math.trunc(emp_salary) }')
print('F''using ceil function, result = {math.ceil(emp_salary) }')
print('F''using ceil function, result = {math.floor(emo_salary)}')
