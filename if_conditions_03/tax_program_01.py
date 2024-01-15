# program to solve net salary
# inputs
emp_name = 'Yahia Momtaz'
emp_gross_salary = 4000

# processing [ calculation ]
if emp_gross_salary >= 5000:
    tax_pct = 10
else:
    tax_pct = 0

emp_net_salary = emp_gross_salary - tax_pct / 100 * emp_gross_salary

# output  : result
#print('Emp net salary = ', emp_net_salary)



# caLculate net salary based on the employee gross salary
# tax 10%  if gross salary => 8000 ,    tax = 0%   if gross salary < 8000


emp_name = 'Mohamed Mazin'
emp_gross_salary = 8000


if emp_gross_salary >= 5000:
    tax = 10
else:
    tax = 0

# calculate net salary equation

emp_whole_salary = emp_gross_salary - emp_gross_salary * tax / 100
print(emp_whole_salary)









#calculate the net salary based on the gross salary
# tax 10% if emp_gross_salary >= 5000   tax 0%  if emp_gross_salary < 5000

emp_name = 'abdalah al fateh'
emp_gross_salary = 10000


if emp_gross_salary >= 5000:
    tax = 10
else:
    tax = 0


# calculate the emp_net_Salary using the known equation

emp_net_salary = emp_gross_salary - emp_gross_salary * tax / 100


print("emp_net_salary = ", emp_net_salary)
print("emp_name = ", emp_name)

print('emp_monthly_salary = ' ,  emp_net_salary)
emp_annual_net_salary = emp_net_salary * 12

print("emp_annual_net_salary = " , emp_annual_net_salary)

