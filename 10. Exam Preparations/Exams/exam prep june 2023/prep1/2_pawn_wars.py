def save_positions(searching_for, index_to_save, r_o_w):    # find positions of the pawns
    if searching_for in board[r_o_w]:
        positions[index_to_save].append(r_o_w)                  # add row of the white pawn
        positions[index_to_save].append(board[r_o_w].index(searching_for))  # add index of the col with 'w' white pawn


SIZE = 8    # define size of the board

# not with comprehension because we have to find positions of the pawns
# board = [[x for x in input().split()] for x in range(SIZE)]
board = []
positions = [[], []]     # white pawn, black pawn

for row in range(SIZE):
    board.append(input().split())       # add rows of the user input

    save_positions('w', 0, row)
    save_positions('b', 1, row)

# if absolute difference of the rows in positions equal 1, the pawns will attack each other in some moment
# if the positions are in the neighbour row
# otherwise no attack will occur
if abs(positions[0][1] - positions[1][1]) != 1:  # if the col difference is not 1 find first pawn that will reach end

    # to find firs pawn tha will go to the end of the board, set both positions on the same side of the board.
    # both pawns will go in the same direction and the pawn with bigger index will go to end of the board first
    # if pos white pawn of the same side   <=  black pawn pos
    if SIZE - positions[0][0] - 1 <= positions[1][0]:       # win condition

        # position of promotion to queen of black pawn is found by ascii value of a - 97 plus col position at row 1
        print(f'Game over! Black pawn is promoted to a queen at {chr(97 + positions[1][1])}1.')
    else:
        # position of promotion to queen of white pawn is found by ascii value of a - 97 plus col position at row 8
        print(f'Game over! White pawn is promoted to a queen at {chr(97 + positions[0][1])}8.')

else:   # if the difference is 1, then pawns will attack each other

    place = (positions[0][0] + positions[1][0]) // 2    # row index pawns meet

    # additional condition: if both pawns are on odd or even row positions, white pawn win
    # if white pawn is on odd row position and black in on even row position and vice versa, black win

    if positions[0][0] % 2 == positions[1][0] % 2:  # if same result of module division by 2, bot are on even pos

        # col letter is ascii value of a plus the col index of the white pawn, cols are from a to h
        # row number is SIZE - place
        print(f'Game over! Black win, capture on {chr(97 + positions[0][1])}{SIZE - place}.')
    else:                                           # else they are on odd and even pos and black pawn win
        print(f'Game over! White win, capture on {chr(97 + positions[1][1])}{SIZE - place}.')

