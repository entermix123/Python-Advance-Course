def idx_in_range(idx):                                      # define function to check if idxs are in range
    return True if 0 <= idx < len(matrix) else False        # return True if in range else False


rows = int(input())             # take rows from input

matrix = []                     # define matrix
temp = []                       # define temporary list

for _ in range(rows):                           # iterate true rows
    temp = [int(x) for x in input().split()]    # iterate true split by space input and make items integers
    matrix.append(temp)                         # add items to temporary list

user = input().split()                          # split next input by space
while user[0] != 'END':                         # while not END
    command = user[0]                           # command is value of zero index in user
    row = int(user[1])                          # row position is integer value of first index in user
    col = int(user[2])                          # col position is integer value of second index in user
    value = int(user[3])                        # value is integer value of third index in user
    if idx_in_range(row) and idx_in_range(col):  # check function if indexes are in range
        if command == 'Add':                    # if command is Add
            matrix[row][col] += value           # add value to the item with the coordinates
        elif command == 'Subtract':             # if command is Subtract
            matrix[row][col] -= value           # subtract value from the item with coordinates
    else:                                       # if indexes are not in range
        print('Invalid coordinates')            # print

    user = input().split()                      # input for while cycle

for row in range(len(matrix)):                      # iterate true final matrix
    print(' '.join(str(x) for x in matrix[row]))    # print items for every row
