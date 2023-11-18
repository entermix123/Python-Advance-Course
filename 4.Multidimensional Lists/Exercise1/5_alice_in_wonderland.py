size = int(input())  # save size of the matrix

matrix = []
alice_pos = []    # def alice position
alice_bag = 0

# creat dict with possible moves positions
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for row in range(size):                 # iterate true matrix rows
    line = input().split()              # split input

    matrix.append(line)                 # add row to matrix

    if 'A' in line:                     # if 'A' in the line
        alice_pos = [row, line.index('A')]  # save alice position
        matrix[row][alice_pos[1]] = '*'     # set position to '*'

while alice_bag < 10:       # while not 10 bags

    command = input()       # read input command

    row = alice_pos[0] + directions[command][0]     # add point to position row from dictionary values
    col = alice_pos[1] + directions[command][1]     # add point to position col from dictionary values

    if not (0 <= row < size and 0 <= col < size):   # check if indexes are in range of the matrix, valid
        break                                       # if not, break

    alice_pos = [row, col]              # save new alice position
    position = matrix[row][col]         # set position value to current position
    matrix[row][col] = '*'              # set position in matrix to '*'

    if position == 'R':                 # if current position is 'R'
        break                           # break cycle

    if position.isdigit():              # if current position is digit
        alice_bag += int(position)      # add value to alice bags

if alice_bag < 10:                      # if alice do not have 10 bags
    print(f"Alice didn't make it to the tea party.")        # print result
else:
    print(f"She did it! She went to the party.")            # else, print result

print(*[' '.join(row) for row in matrix], sep='\n')         # print matrix
