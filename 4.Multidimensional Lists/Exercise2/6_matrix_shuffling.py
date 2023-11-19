rows, cols = tuple(map(int, input().split()))    # take rows and cols from input

matrix = [input().split() for _ in range(rows)]    # make matrix from input

while True:
    line = input()

    if line == 'END':        # break cycle condition
        break

    command = line.split()[0]  # def command

    if command != 'swap' or len(line.split()) != 5:    # invalid input conditions
        print(f'Invalid input!')                        # print
        continue                                        # go to next cycle

    # make variables for coordinates from input
    row_1 = int(line.split()[1])
    col_1 = int(line.split()[2])
    row_2 = int(line.split()[3])
    col_2 = int(line.split()[4])

    if not (0 <= row_1 < rows and 0 <= col_1 < cols) and not (0 <= row_2 < rows and 0 <= col_2 < cols):
        print(f'Invalid input!')  # print
        continue  # go to next cycle

    # swap places of the two values
    temp_1 = matrix[row_2][col_2]
    temp_2 = matrix[row_1][col_1]

    # save new values to the matrix
    matrix[row_1][col_1] = temp_1
    matrix[row_2][col_2] = temp_2

    for row in matrix:                                          # iterate true matrix
        # print(' '.join(list(map(str, row))))  # print result    # print every row in matrix
        print(*row)
