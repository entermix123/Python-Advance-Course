
# file = 'text.txt'                 # save file to variable
#
# try:                              # try
#     file = open(file, 'r')        # open file read
#     print('File found')           # if file si opened print result
# except FileNotFoundError:         # if file is not found
#     print('File not found')       # print result


# current_file = open('1_file_open.py', 'r')      # save current file in variable
# print(current_file.read())                      # print current file with method .read()
#
# for num in range(1, 5):                         # additional code visualized with results
#     print(num)


# current_file = open('1_file_open.py', 'r')      # save current file in variable
# print(current_file.readline())                      # print current file with method .read()


# current_file = open('1_file_open.py', 'r')      # save current file in variable
# for line in current_file:                       # iterate true file lines
#     data = line.split()                         # split every line by space
#     print(data)                                 # print all in the line as a list


# def read_file_line_by_line(file_name):      # def of function for reading file line by line
#     current_file = open(file_name, 'r')     # make variable and open file_name to read
#     for line in current_file:               # iterate true file and take line
#         data = line.split()                 # make data variable and take split line as a list
#         print(data)                         # print data
#
#
# read_file_line_by_line('1_file_open.py')    # call function for path and file name

