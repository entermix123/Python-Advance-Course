# from string import punctuation  # import all signs --> punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
#
# with open('text.txt', 'r') as file:     # open sorce file
#     data = file.readlines()             # create list data with every row as item
#
# out_file = open('output.txt', 'w')      # open/create output file
#
# for i in range(len(data)):              # iterate true data list
#     row = data[i]                       # add content to row variable
#
#     letters = 0                         # create counter of letters
#     puncts = 0                          # create counter of signs
#
#     for letter in row:                  # iterate true row
#
#         if letter.isalpha():            # if item is letter
#             letters += 1                # add point to letters
#
#         elif letter in punctuation:     # if item is sign
#             puncts += 1                 # add point to signs
#
#     # when we slice ([:-1]), sorce text should have empty last row, so we do not miss last symbol.
#     out_file.write(f'Line {i+1}: {"".join(row[:-1])} ({letters})({puncts})\n')
#
# out_file.close()

from string import punctuation  # import all signs --> punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

with open('text.txt', 'r') as file:     # open sorce file
    data = file.readlines()             # create list data with every row as item

    out_file = open('output.txt', 'w')  # open output file to write

    for i in range(len(data)):              # iterate true data list
        row = data[i]                       # add content to row variable

        letters = 0                         # create counter of letters
        puncts = 0                          # create counter of signs

        for letter in row:                  # iterate true row

            if letter.isalpha():            # if item is letter
                letters += 1                # add point to letters

            elif letter in punctuation:     # if item is sign
                puncts += 1                 # add point to signs

        # when we slice ([:-1]), sorce text should have empty last row, so we do not miss last symbol.
        out_file.write(f'Line {i+1}: {"".join(row[:-1])} ({letters})({puncts})\n')

out_file.close()    # close output file !!!

# When we work over one file continuously, we should not use 'with open(file)', but var = open(file, 'w'),
# work on it and then var = close()

