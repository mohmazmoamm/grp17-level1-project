# find if a number found in a list or not ?
num = 7
my_list = [5, 2, 1, 7, 8, 20, 7, 3]
index_list = []

is_found = 'n'
index = -1

for i in range(len(my_list)):
    if my_list[i] == num:
        is_found = 'y'
        index_list.append(i)

if is_found == 'y':
    print('item found at index = ', index_list)
else:
    print('item is not found in the list')