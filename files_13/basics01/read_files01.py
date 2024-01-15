# program to read from text files

# 1. first we open the file
# 2. we read the file
# 3. we close the file

print('----- first way -----')
my_file = open('C:\\MY_FILES\\read_data.txt',  'r')
content = my_file.read()
print(content)
my_file.close


print('---- second way using with ---ignore close ------')
with open('C:\\MY_FILES\\read_data.txt', 'r') as my_file:
    content = my_file.read()
    print(content)

print('end')



