import os
import re

'''CAREFUL WITH USING THIS! CAN RENAME FILES AND DIRS THAT CAN NOT BE RUN IN SOME SOFTWARE AFTER'''

directory = input('Enter the directory: ')                      # user input directory
string_to_replace = input('Enter a string to replace: ')        # symbol or string to be replaced
string_to_replace_with = input('Enter the string that you want to replace with: ')      # symbol or string to replace with

for filename in os.listdir(directory):              # iterate true items in directory
    file = os.path.join(directory, filename)    # dir_name + '/' + filename, take path of the item (filename

    if os.path.isfile(file):                                                        # if item is file
        new_name = filename.replace(string_to_replace, string_to_replace_with)      # replace old with new string from input

        # usage of regex to take all strings except slashes and last index and append new name
        new_file = "/".join(re.split(r"[\\/]]", file))[:-1] + "/" + new_name

        os.rename(file, new_file)   # rename file with same path and the new name
