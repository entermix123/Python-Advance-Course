size = int(input())     # save size of the matrix

matrix = [input().split(', ') for x in range(size)]     # create and fill up matrix
primary, secondary = [], []                             # create primary and secondary list

for idx in range(size):                                 # iterate true size
    primary.append(matrix[idx][idx])                    # add item to primary list
    secondary.append(matrix[idx][size - idx - 1])       # add item to secondary list

print(f"Primary diagonal: {', '.join(primary)}. Sum: {sum(map(int, primary))}")     # print result
print(f"Secondary diagonal: {', '.join(secondary)}. Sum: {sum(map(int, secondary))}")   # print result

