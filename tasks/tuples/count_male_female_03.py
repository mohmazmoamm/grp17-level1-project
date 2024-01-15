# H.w No. 3: # Count and print no. of Male, no. of Female in this List of Tuples
company_employees = [
    (101, 'Hayam Esam', 10000.0, 'Engineer', 'F'),
    (102, 'Ibrahim Ahmed', 9000.0, 'Accountant','M'),
    (103, 'Adham Aly', 5000.0, 'Engineer', 'M'),
    (104, 'Islam Hasan', 7000.0, 'Sales', 'M'),
    (104, 'Marwa Esam', 7000.0, 'Marketer', 'F'),
    (104, 'Ola Hasan', 7000.0, 'Engineer', 'F')
]
male_count = 0
female_count = 0
for item in company_employees:
    if item[4] == 'M':
        male_count += 1
    elif item[4] == 'F':
        female_count += 1

print('Male = ', male_count, 'Female Count = ', female_count)