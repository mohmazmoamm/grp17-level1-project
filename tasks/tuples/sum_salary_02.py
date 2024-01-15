# H.w No. 2: # print sum of salary of all employees – from tuples from the list
company_employees = [
    (101, 'Ahmed Esam', 10000.0, 'Cairo'),
    (102, 'Ibrahim Ahmed', 9000.0, 'Cairo'),
    (103, 'Adham Aly', 5000.0, 'Cairo'),
    (104, 'Islam Hasan', 7000.0, 'Cairo')
]
sum = 0
for item in company_employees:
    sum = sum + item[2]

print('sum = ', sum)