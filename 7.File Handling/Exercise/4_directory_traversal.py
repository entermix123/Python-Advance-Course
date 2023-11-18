import os           # import os for delete file


def save_extensions(dir_name, first_level=False):   # first_level=False --> at the start
    for filename in os.listdir(dir_name):           # iterate true user input path
        file1 = os.path.join(dir_name, filename)    # dir_name + '/' + filename

        if os.path.isfile(file1):                   # check if item is file
            extension1 = filename.split('.')[-1]    # if it is a file, take the extension

            if extension1 not in extensions:        # if current extension is not in extension dictionary
                extensions[extension1] = []         # make new key-value pair in dictionary

            extensions[extension1].append(filename)         # append extension to dictionary

        elif os.path.isdir(file1) and not first_level:      # if item is directory
            save_extensions(file1, first_level=True)        # enter next level "recursion bottom"


directory = input()             # user input of the path of the searched directory
result = []                     # create result list
extensions = {}                 # create dictionary as extension and file register
save_extensions(directory)      # call function

extensions = sorted(extensions.items(), key=lambda x: x[0])     # sort data in dictionary by key, ascending as a list of tuples

for extension, files in extensions:     # extensions = key, files = value, iterate true dictionary (list of tuples)
    result.append(f'.{extension}')      # add extension as item in result list

    for file in sorted(files):          # iterate true files in values of the dictionary --> nested directory files
        result.append(f'---{file}')     # add items as nested level items

with open('report.txt', 'w') as file:   # create report.txt file
    file.write('\n'.join(result))       # on every row write items from result list
