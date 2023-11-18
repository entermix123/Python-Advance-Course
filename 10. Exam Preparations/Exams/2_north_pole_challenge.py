rows, cols = input().split(', ')

matrix = []
position = []
items_on_map = {'D': 0, 'G': 0, 'C': 0}     # create dictionary for possible items in matrix
collected = {'D': 0, 'G': 0, 'C': 0}        # create dictionary for collected items

for row in range(int(rows)):                # iterate in range of rows
    line = input().split()                  # split input for every row

    if "Y" in line:                         # check if "Y" is in the line
        position = [row, line.index("Y")]   # set the start position

    if 'G' in line:                             # check if 'G' in line
        items_on_map['G'] += line.count('G')    # add count of 'G' in the line to items in matrix dictionary
    if 'D' in line:                             # check if 'D' in line
        items_on_map['D'] += line.count('D')    # add count of 'D' in the line to items in matrix dictionary
    if 'C' in line:                             # check if 'C' in line
        items_on_map['C'] += line.count('C')    # add count of 'C' in the line to items in matrix dictionary

    matrix.append(line)                         # add line to matrix

matrix[position[0]][position[1]] = "x"          # set start position symbol to x

win = False             # set win condition

moves = {               # create option with possible moves coordinates
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

line = input()                          # take command line
command = line.split('-')[0]            # split command direction
count_moves = int(line.split('-')[1])   # split command count

while True:

    matrix[position[0]][position[1]] = 'x'  # set current position symbol to 'x' when start to move

    for x in range(count_moves):            # iterate true direction in range of commands count

        position[0] = position[0] + moves[command][0]   # add row coordinates for next move
        if position[0] == int(rows):                    # check if out of range up for rows
            position[0] = 0                             # set next position row to 0
        elif position[0] < 0:                           # check if out of range down for rows
            position[0] = int(rows) - 1                 # set next position row to max rows - 1

        position[1] = position[1] + moves[command][1]   # add col coordinates for next move
        if position[1] == int(cols):                    # check if out of range right for cols
            position[1] = 0                             # set next position row to 0
        elif position[1] < 0:                             # check if out of range left for cols
            position[1] = int(cols) - 1                 # set next position row to max col - 1

        if matrix[position[0]][position[1]] == "D":     # check if next position is Decoration
            collected["D"] += 1                         # add point in collected dictionary
            matrix[position[0]][position[1]] = "x"      # set the position in the matrix to 'x'

        elif matrix[position[0]][position[1]] == "C":   # check if next position is Cookies
            collected["C"] += 1                         # add point in collected dictionary
            matrix[position[0]][position[1]] = "x"      # set the position in the matrix to 'x'

        elif matrix[position[0]][position[1]] == "G":   # check if next position is	Gifts
            collected["G"] += 1                         # add point in collected dictionary
            matrix[position[0]][position[1]] = "x"      # set the position in the matrix to 'x'

        elif matrix[position[0]][position[1]] == ".":   # check if next position is	empty
            matrix[position[0]][position[1]] = "x"      # set the position in the matrix to 'x'

        if collected.items() == items_on_map.items():   # check if all items are collected
            print("Merry Christmas!")                   # print result
            win = True                                  # set win condition to True
            break                                       # break 'for' cycle

    matrix[position[0]][position[1]] = 'Y'              # set current position in matrix to 'Y' when stop current moves

    if win:         # if win condition is triggered
        break       # break while cycle

    line = input()      # take next command
    if line == "End":   # check if command == 'End'
        break           # break while cycle

    command = line.split('-')[0]            # take command direction
    count_moves = int(line.split('-')[1])   # take command count

# set result list with strings
result = ["You've collected:", f'- {collected["D"]} Christmas decorations', f'- {collected["G"]} Gifts',
          f'- {collected["C"]} Cookies']

# print result list
print('\n'.join(result))

# print matrix
for row in matrix:
    print(' '.join(x for x in row))
