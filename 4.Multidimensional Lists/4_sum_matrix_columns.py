rows, columns = [int(x) for x in input().split(', ')]

matrix = []
for row in range(rows):                                         # creation of the matrix
    matrix.append([int(x) for x in input().split()])            # filling of the matrix

for col in range(columns):                                      # iterate true columns first
    total = 0                                                   # reset total sum for every index in column
    for row in range(rows):                                     # for same index in column iterate true rows
        total += matrix[row][col]                               # sum all items in same index in column for every row
    print(total)                                                # print the sum

