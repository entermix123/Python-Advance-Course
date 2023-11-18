import os
#
# os.remove('file_name.txt')          # local path
# os.remove('D/..../file_name.txt')   # full path

# file_path = 'readme123.txt'     # specify file
#
# if os.path.exists(file_path):   # if file exist
#     os.remove(file_path)        # delete file

# file_path = 'readme123.txt'       # specify file path and name
# try:                              # try check if possible
#     os.remove(file_path)          # remove file
#     print('File removed!')        # print if file is removed
# except FileNotFoundError as err:  # if file do not exist raise error
#     print(err)                    # print error
