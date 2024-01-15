rejected_ips = [
    ('192.168.0.15', 'y'),
    ('192.168.0.22', 'y'),
    ('192.168.0.14', 'y'),
    ('192.168.0.24', 'n'),
    ('192.168.0.81', 'n'),
    ('192.168.0.11', 'y')
]

print(rejected_ips)
print(rejected_ips[0])
print(rejected_ips[0][1])
print('------- printing only allowed ips [ y ] ----')
for item in rejected_ips:
    if item[1] == 'y':
        print(item, item[0], item[0][-2:], item[0][rejected_ips[0][0].rfind('.') + 1:])

print(rejected_ips[0][0])
print(rejected_ips[0][0].rfind('.'))