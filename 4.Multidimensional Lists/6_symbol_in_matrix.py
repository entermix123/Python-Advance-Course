size = int(input())     # take size of the matrix from input - integer

matrix = []             # create empty matrix
found = False           # set found condition

for _ in range(size):                       # iterate true rows
    matrix.append([x for x in input()])     # add items to the matrix

char = input()                              # take searched char from input

for row in range(size):                     # iterate true matrix rows
    for col in range(size):                 # for every row iterate true columns
        if matrix[row][col] == char:        # if searched character is the item
            print(f'({row}, {col})')        # print the location in the matrix
            found = True                    # trigger found flag
            break                           # exit cycle for the columns
    if found:                               # if character is found, exit cycle for rows
        break

if not found:                                       # if found flag not triggered
    print(f'{char} does not occur in the matrix')   # print negative result
