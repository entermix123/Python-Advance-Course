size = int(input())                             # take size of the matrix
matrix = [list(input()) for _ in range(size)]   # creating matrix

positions = ((-2, 1), (-2, -1), (-1, 2), (-1, -2), (2, 1), (2, -1), (1, 2), (1, -2))  # all possible moves for the horse

removed_horses = 0      # how many horses are removed

while True:

    max_attacks = 0                 # max attack counter
    knight_max_attacks_pos = []     # position of the horse with max attacks

    for row in range(size):         # iterate true matrix
        for col in range(size):     # iterate true columns
            if matrix[row][col] == 'K':     # if position is horse
                attack = 0                  # set attacks to zero

                for cur_pos in positions:   # iterate true possible moves
                    attack_pos_row = row + cur_pos[0]       # current row + move row position
                    attack_pos_col = col + cur_pos[1]       # current column + move column position

                    if 0 <= attack_pos_row < size and 0 <= attack_pos_col < size:   # if move positions in range of the matrix
                        if matrix[attack_pos_row][attack_pos_col] == 'K':           # if move position is also horse
                            attack += 1                                             # add 1 attack to current horse

                if attack > max_attacks:                    # if current horse is with more attack from max attack horse
                    knight_max_attacks_pos = [row, col]     # save position of the current horse as max attack horse
                    max_attacks = attack                    # save attacks to max attacks

    if knight_max_attacks_pos:                              # if nay max horse
        matrix[knight_max_attacks_pos[0]][knight_max_attacks_pos[1]] = '0'  # set position to value from 'K' to '0'
        removed_horses += 1                                 # add 1 to removed horses
    else:                                                   # if no more horses with higher attack
        break                                               # break while cycle

print(removed_horses)                                       # print count removed horses
