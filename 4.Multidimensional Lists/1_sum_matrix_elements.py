# input:
# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0

# comprehension of two-dimensional matrix only! input only 2 digits! Unpack input !
rows, cols = [int(x) for x in input().split(', ')]

matrix = []
sum1 = 0

for _ in range(rows):                                       # create rows
    matrix.append([int(x) for x in input().split(', ')])    # fill up the columns in matrix from input

for row_idx in range(rows):                                 # iterate true rows in the matrix
    for col_idx in range(cols):                             # for every row, iterate true columns in the matrix
        sum1 += matrix[row_idx][col_idx]                    # add values in sum1 for every element in the column

print(sum1)                                                 # print sum1
print(matrix)                                               # print matrix
