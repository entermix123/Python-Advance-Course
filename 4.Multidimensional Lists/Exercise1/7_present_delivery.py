def if_cookies(presents_left, nice_kids_visit1):
    for moves in possible_cookie_moves.values():    # iterate true dict with possible moves
        row1 = santa_loc[0] + moves[0]              # for every move add row position
        col1 = santa_loc[1] + moves[1]              # for every col add col position

        if matrix[row1][col1].isalpha():            # if moved position is char
            if matrix[row1][col1] == nice_kid:      # if moved position is nice kid house
                nice_kids_visit1 += 1               # add 1 to visited nice kids count

            matrix[row1][col1] = '-'                # make visited house '-'
            presents_left -= 1                       # subtract 1 present
    return presents_left, nice_kids_visit1           # return presents and nice kids visited count


presents = int(input())     # count presents
size = int(input())         # size of the matrix

matrix = [[x for x in input().split()] for _ in range(size)]    # fill matrix

santa_loc = []      # create santa location list
naughty_kid = 'X'   # bad kid house
nice_kid = 'V'      # good kid house
total_nice_kids = 0
nice_kids_visit = 0
cookies = 'C'       # cookies house
santa = False       # found santa flag
possible_cookie_moves = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}   # create dictionary for moves
check_house_row = [0, 0]


for row in range(size):                 # iterate true matrix rows
    for col in range(size):             # iterate true matrix cols
        if matrix[row][col] == 'S':     # find santa location
            santa_loc = [row, col]      # save santa location
            matrix[row][col] = '-'      # replace santa position with '-'
        elif matrix[row][col] == nice_kid:  # check for nice kid house
            total_nice_kids += 1            # if nice kid house add 1 to nice kids count

command = input()
while command != 'Christmas morning':     # while command is different of 'Christmas morning'

    santa_loc = [
        santa_loc[0] + possible_cookie_moves[command][0],   # find santa new position row
        santa_loc[1] + possible_cookie_moves[command][1]    # find santa new position col
    ]

    house = matrix[santa_loc[0]][santa_loc[1]]              # set house visiting

    if house == nice_kid:           # if house is with nice kid
        nice_kids_visit += 1        # add 1 to count nice kids
        presents -= 1               # subtract 1 present

    elif house == cookies:          # if house is with cookies
        presents, nice_kids_visit = if_cookies(presents, nice_kids_visit)   # function if_cookies

    matrix[santa_loc[0]][santa_loc[1]] = '-'    # replace visited house with '-'

    if not presents or nice_kids_visit == total_nice_kids:  # if there is no presents or nice kids to visit, break cycle
        break

    command = input()       # read input

matrix[santa_loc[0]][santa_loc[1]] = 'S'    # set santa position to last house he visited

if not presents and nice_kids_visit < total_nice_kids:  # if no present and there are nice kids
    print(f'Santa ran out of presents!')                # print result

print(*[' '.join(row) for row in matrix], sep='\n')     # print all rows in matrix on new line for every row

if nice_kids_visit == total_nice_kids:                  # if all nice kids are visited
    print(f'Good job, Santa! {nice_kids_visit} happy nice kid/s.')      # print result
else:
    print(f'No presents for {total_nice_kids - nice_kids_visit} nice kid/s.')
