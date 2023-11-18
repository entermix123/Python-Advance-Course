def move(direction, steps):         # definition of move command function
    m = my_position[0] + (possible_directs[direction][0] * steps)   # change current position row with direction and steps
    k = my_position[1] + (possible_directs[direction][1] * steps)   # change current position column with direction and steps

    if not (0 <= m < size and 0 <= k < size):     # if indexes in range, valid
        return my_position                        # return new position

    if matrix[m][k] == 'x':                       # if position is target
        return my_position                        # return last position

    return [m, k]                                 # if indexes are valid and position is not target, return new position


def shoot(direction):                             # definition of shoot command function
    m = my_position[0] + possible_directs[direction][0]     # change target position row with direction and steps
    k = my_position[1] + possible_directs[direction][1]     # change target position col with direction and steps

    while 0 <= m < size and 0 <= k < size:      # if indexes are in range of the matrix, valid
        if matrix[m][k] == 'x':                 # if position in matrix in 'x'
            matrix[m][k] = '.'                  # replace target mark with '.'
            return [m, k]                       # return position of shoot target

        m += possible_directs[direction][0]     # add next position target row
        k += possible_directs[direction][1]     # add nex position target col


size = 5        # set size of the matrix
matrix = [[x for x in input().split()] for _ in range(size)]        # fill up matrix

total_targets = 0   # def total targets
hits = 0            # def hit targets
hits_pos = []       # def list of hit targets positions

my_position = []    # def current position

# creat dict with possible moves positions
possible_directs = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for row in range(size):         # iterate true matrix rows
    for col in range(size):     # iterate true matrix cols
        if matrix[row][col] == 'A':     # if position is 'A'
            my_position = [row, col]    # save found my position
            matrix[row][col] = '.'      # remove sigh of my position

        if matrix[row][col] == 'x':     # if position is target 'x'
            total_targets += 1          # add point to total target

for _ in range(int(input())):           # save number of commands
    command = input().split()           # input command

    if command[0] == 'move':                                # if move command
        my_position = move(command[1], int(command[2]))     # change position true move function

    elif command[0] == 'shoot':                             # if shoot position
        target_down_position = shoot(command[1])            # save target position

        if target_down_position:                            # if any target hit
            hits_pos.append(target_down_position)           # add hit position to list
            hits += 1                                       # add point to hits

        if hits == total_targets:                           # if all targets are hit
            print(f'Training completed! All {hits} targets hit.')   # print result
            break                                                   # break the cycle

if hits < total_targets:    # if not all targets hit
    print(f'Training not completed! {total_targets - hits} targets left.')  # print

[print(target_pos) for target_pos in hits_pos]  # print targets positions
