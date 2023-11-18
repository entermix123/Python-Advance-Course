# lines = ['Readme', 'This is my Github repository']      # input
#
# with open('readme.txt', 'w') as file:                   # create file
#     for line in lines:                                  # iterate true input
#         file.write(line)                                # write input into file
#         file.write('\n')                                # new line after every input line


# more_lines = ['', 'append text files', 'the end']           # next input
#
# with open('readme.txt', 'a') as file:                       # open file
#     file.write('\n'.join(more_lines))                       # append next input


# def write_data_to_file(file, mode):                     # define function write
#     current_file = open(file, mode)                     # open or create file
#     current_file.write('''This is just example!:\n      # write file with info
#                        First line,
#                        second line,
#                        third line,
#                        end line !!!''')
#
#
# write_data_to_file('new_file_example.txt', 'w')         # call function with file name and mode

# list1 = ['This is example 1 \n', 'This is example 2 \n', 'This is example 3 \n']    # input
#
# with open('new_file_example1', 'w') as file:                                        # create file
#     file.write('list content \n')                                                   # write first line
#     file.writelines(list1)                                                          # write input

# with open('example3.txt', 'a') as file:             # open or create file
#     file.write('\n Append example')                 # append info in it


# file_path = 'text1.txt'                       # create variable with file name
#
# content = 'I just created my first file'      # input
#
# with open('text1.txt', 'w') as file:          # open/create file
#     file.write(content)                       # add content to file
