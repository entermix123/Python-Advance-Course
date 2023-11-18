rows, cols = map(int, input().split())      # create rows and cols from input

matrix = [input().split() for _ in range(rows)]     # fill the matrix

count_cubes = 0                         # create count searched cubes

for idx in range(rows - 1):             # iterate true rows in matrix
    for idx1 in range(cols - 1):        # iterate true cols in matrix
        # if all nex elements are the same - in next column, next row same column and next row, next column
        if matrix[idx][idx1] == matrix[idx][idx1 + 1] and matrix[idx][idx1] == matrix[idx + 1][idx1] \
                and matrix[idx][idx1] == matrix[idx + 1][idx1 + 1]:
            count_cubes += 1    # add point to count found cubes
print(count_cubes)              # print count cubes
