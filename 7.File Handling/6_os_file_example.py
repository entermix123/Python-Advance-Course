import os

# print(os.getcwd())        # present current directory
# print(os.mkdir('D:\Python Projects\Python Advanced SoftUni September 2022\created_files'))  # make directory to path
# os.mkdir('examples')      # make directory in current directory
# os.remove('some_file')      # delete specified file
# print(os.listdir(os.getcwd()))  # print content in current directory in list

# dir1 = os.listdir(os.getcwd())  # create variable that contains all items in current directory
# for file in dir1:               # iterate true variable
#     print(file)                 # print every item in the directory


# file_path = 'readme123.txt'       # specify file path and name
# try:                              # try check if possible
#     os.remove(file_path)          # remove file
#     print('File removed!')        # print if file is removed
# except FileNotFoundError as err:  # if file do not exist raise error
#     print(err)                    # print error
