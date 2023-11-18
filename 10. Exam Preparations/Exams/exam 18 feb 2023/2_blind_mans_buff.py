def make_move(old_pos, new_pos):        # create function for make a move
    new_position = [[], []]
    new_position[0] = old_pos[0] + new_pos[0]
    new_position[1] = old_pos[1] + new_pos[1]
    return new_position


rows, cols = [int(x) for x in input().split()]      # take user input for rows and cols of the matrix

matrix = []                                         # create empty matrix
current_position = []                               # create current position
next_position = [[], []]                            # create next position list
for row in range(rows):                             # iterate in range rows
    line = input().split()                          # save user input split by space
    if 'B' in line:                                 # check if star position is in line
        current_position = [row, line.index('B')]   # if in line save it in current position

    matrix.append(line)                             # append line to matrix

matrix[current_position[0]][current_position[1]] = '-'  # make start position '-'

moves = {               # create dictionary with possible moves directions
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

moves_made = 0          # create variable for moves made
touched_players = 0     # create variable for players touched

command = input()           # take command from user input
while command != 'Finish':  # if command is 'Finish', break the cycle

    if touched_players == 3:    # if reach 3 touched players, break the cycle
        break

    next_position[0] = current_position[0] + moves[command][0]  # set next move position row
    next_position[1] = current_position[1] + moves[command][1]  # set next move position col

    # if next position is out of matrix or obstacle
    if next_position[0] >= rows or next_position[0] < 0 or next_position[1] >= cols or next_position[1] < 0 or\
            matrix[next_position[0]][next_position[1]] == 'O':
        next_position = [[], []]                            # set empty next position ( ignore the command )

    elif matrix[next_position[0]][next_position[1]] == '-':                 # if next move is empty
        current_position = make_move(current_position, moves[command])      # make the move
        moves_made += 1                                                     # add point to moves made

    elif matrix[next_position[0]][next_position[1]] == 'P':                 # if next move is player
        touched_players += 1                                                # add point to touched players
        matrix[next_position[0]][next_position[1]] = '-'                    # made the position empty
        current_position = make_move(current_position, moves[command])      # make the move
        moves_made += 1                                                     # add point to moves made

    command = input()     # take next command


# print results
print(f"Game over!")
print(f"Touched opponents: {touched_players} Moves made: {moves_made}")
