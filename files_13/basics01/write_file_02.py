# program to write into text file

# 1.open for wrtie
# 2. write
# 3. close

print('------- first way -----')
my_file = open('C:\\MY_FILES\\write_data.txt', 'w')
my_file.write(' I like programming\n')
my_file.write(' I like Football\n')
my_file.write(' Python is a Programming Language')
my_file.close()


print('------- second way ----------- using with ---')
with open ('C:\\MY_FILES\\write_data.txt', 'a') as my_file:
    my_file.write('\n')
    my_file.write(' My city is Cairo\n')
    my_file.write(' My city is Alex\n')
    my_file.write(' Iam a SW Engineer')



