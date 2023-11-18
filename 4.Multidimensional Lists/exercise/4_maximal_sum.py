rows, cols = map(int, input().split())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

sum_matrix = 0          # def sum matrix
max_sum = -9999999      # set minimum value of max sum
max_sum_matrix = []     # def empty max sum matrix

for row in range(rows - 2):                 # iterate true rows - 2 to prevent out of range error
    for col in range(cols - 2):             # iterate true columns - 2 to prevent out of range error
        # find sum of current 3x3 matrix
        sum_matrix = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] \
                     + matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] \
                     + matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]

        if max_sum < sum_matrix:    # if max sum < of sum current matrix
            max_sum = sum_matrix    # set max sum to sum of current matrix
            # set max sum matrix to current matrix
            max_sum_matrix = [[matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
                              [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
                              [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]]

print(f'Sum = {max_sum}')  # print max sum
for row in max_sum_matrix:                  # iterate true max result matrix
    print(' '.join(list(map(str, row))))    # print items



