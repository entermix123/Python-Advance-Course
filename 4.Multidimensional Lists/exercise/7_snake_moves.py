rows, cols = tuple(map(int, input().split()))   # take integers of rows and columns from input
snake = input()                                 # take snake input

matrix = []                     # create empty matrix
idx = 0                         # set index to 0
for row in range(rows):         # iterate true rows
    result = ''                 # set result to empty string
    for col in range(cols):                 # iterate true columns
        result += snake[idx % len(snake)]   # add chars to result string for idx module divided of length of the snake
        idx += 1                            # add point to snake

    if row % 2 == 0:                        # for every even row
        matrix.append(result)               # add the result to list
    else:                                   # for every odd row
        matrix.append(result[::-1])         # add the reversed result to the list

for substr in matrix:                       # iterate true matrix rows
    print(*substr, sep='')                  # print all items in row
