size = int(input())

# matrix = []             # matrix definition

# one line solution to create the matrix from input if we know how many rows
matrix = [[int(x) for x in input().split()] for _ in range(size)]

# for _ in range(size):                                   # for cycle to fil the matrix
#     matrix.append([int(x) for x in input().split()])    # add items to every row in the matrix


sum1 = 0                        # sum of primary diagonal
for idx in range(size):         # cycle for rows, and don't have to iterate true the column
    sum1 += matrix[idx][idx]    # add item to sum, and for every next row add next item

print(sum1)                     # print sum
