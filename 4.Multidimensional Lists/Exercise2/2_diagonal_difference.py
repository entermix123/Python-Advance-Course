size = int(input())     # save size of matrix

matrix = [input().split() for x in range(size)]         # create matrix from input
primary, secondary = [], []                             # create primary and secondary list

for idx in range(size):                                 # iterate true size
    primary.append(matrix[idx][idx])                    # add item to primary list
    secondary.append(matrix[idx][size - idx - 1])       # add item to secondary list

result = abs(sum(map(int, primary)) - sum(map(int, secondary)))  # find absolute of subtraction of primary and secondary

print(result)   # print(result)
