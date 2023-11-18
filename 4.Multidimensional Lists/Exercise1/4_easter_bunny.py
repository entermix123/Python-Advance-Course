size = int(input())     # save size of matrix

bunny_pos = []          # def bunny position
matrix = []             # def matrix
best_path = []          # def best path
best_direction = False  # set best direction flag
max_eggs = 0            # def max eggs integer

# dict with possible moves positions
moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for row in range(size):         # iterate true matrix size
    line = input().split()      # read input
    if 'B' in line:             # check if rabbit is in line
        bunny_pos = [row, line.index('B')]  # save rabbit position
    matrix.append(line)     # add line to matrix

for directions, positions in moves.items():     # iterate true dictionary of muves
    row, col = [                                # split and add points to position rows nad cols
        bunny_pos[0] + positions[0],
        bunny_pos[1] + positions[1]
    ]

    path = []               # def current path
    collected_eggs = 0      # set current collected eggs

    while 0 <= row < size and 0 <= col < size:  # while indexes are in range
        if matrix[row][col] == 'X':             # if current position is trap - 'X'
            break                               # break cycle

        collected_eggs += int(matrix[row][col])     # add eggs to current collected eggs
        path.append([row, col])                     # set path to current path

        row += positions[0]             # add points to row to reach nex position in the path
        col += positions[1]             # add points to col to reach nex position in the path

    if collected_eggs >= max_eggs:      # if collected eggs in current path are more than max eggs
        max_eggs = collected_eggs       # set max eggs to current collected eggs
        best_direction = directions     # set best direction to current direction
        best_path = path                # set best path to current path

print(best_direction)                   # print best direction
print(*best_path, sep='\n')             # print best path coordinates
print(max_eggs)                         # print max collected eggs

