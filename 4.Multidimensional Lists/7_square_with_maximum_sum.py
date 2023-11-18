rows, cols = [int(x) for x in input().split(', ')]      # save rows and columns length

highest = 0                                             # highest sum definition
matrix = []                                             # matrix definition
cubicle = []                                            # highest sum cubicle

# matrix = [[x for x in input().split(', ')] for lis in range(rows)]  # comprehension solution in one line

for _ in range(rows):                                       # cycle for filling up teh matrix
    matrix.append([int(x) for x in input().split(', ')])    # add items to the matrix

for row in range(rows - 1):                                 # iterate true the matrix rows in range "-1"
    for col in range(cols - 1):                             # iterate true matrix columns in range "-1"
        # find sum of the items in cubicle
        sum_quad = matrix[row][col] + matrix[row][col+1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if sum_quad > highest:                              # if the sum of the current cubicle is higher than last highest sum
            highest = sum_quad                              # make current cubicle highest sum
            # save cubicle
            cubicle = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]]

print(f'{" ".join(str(x) for x in cubicle[:len(cubicle) // 2])}\n'      # print items in half rows
      f'{" ".join((str(x) for x in cubicle[len(cubicle) // 2:]))}')     # print items in other half rows
print(highest)                                                          # print highest sum
