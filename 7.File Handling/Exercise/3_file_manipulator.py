import os
while True:     # create loop for user input

    command, *info = input().split('-')     # split user input by '-'

    if command == 'End':                    # if command is 'End' stop the loop
        break

    if command == 'Create':                 # if command is 'Create'
        file = open(info[0], 'w')           # create file
        file.close()                        # close() --> save file

    if command == 'Add':                    # if command is 'Add'
        with open(info[0], 'a') as file:    # create file
            file.write(f'{info[1]}\n')      # write content in it and close() --> 'with open(...)' also closes (save) file

    if command == 'Replace':                        # if command is 'Replace'
        try:                                        # Try to execute
            with open(info[0], 'r') as file:        # open file
                text = file.read()                  # read lines in file and make string text

            text = text.replace(info[1], info[2])     # replace new value by old value and save string

            with open(info[0], 'w') as file:                    # open to write
                file.write(text)                                # write text as a string

        except FileNotFoundError:                               # if error occur
            print('An error occurred')                          # print custom error

    if command == 'Delete':                     # if command is 'Delete'
        try:                                    # try
            os.remove(info[0])                  # delete file
        except FileNotFoundError:               # if file is not found
            print('An error occurred')          # print custom error

# input1
# Create-file.txt
# Add-file.txt-First Line
# Add-file.txt-Second Line
# Replace-random.txt-Some-some
# Replace-file.txt-First-1st
# Replace-file.txt-Second-2nd
# Delete-random.txt
# Delete-file.txt
# End
