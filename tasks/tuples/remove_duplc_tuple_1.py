# 1: # Remove duplicates from a List of Tuples : Make it unique List

company_ips = [
    ('192.168.0.15', 'y'),
    ('192.168.0.22', 'y'),
    ('192.168.0.14', 'y'),
    ('192.168.0.24', 'n'),
    ('192.168.0.15', 'y'),
    ('192.168.0.11', 'y')
]
unique_list = []
for item in company_ips:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)
company_ips = unique_list
print(unique_list)