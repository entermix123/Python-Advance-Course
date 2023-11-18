rows, cols = list(map(int, input().split()))    # split and make integers from input for rows and cols

# input: 4 6

matrix = []             # def empty matrix
first_letter = 97       # first char is 'a'

for row in range(rows):         # iterate true rows
    sub_list = []               # create sublist
    for col in range(cols):     # iterate true columns
        result = chr(first_letter + row) + chr(first_letter + col + row) + chr(first_letter + row)  # make string
        sub_list.append(result)     # add result string to sublist
    matrix.append(sub_list)         # add sublist to matrix

for row in matrix:                  # iterate true max result matrix
    print(' '.join(list(map(str, row))))    # print result
