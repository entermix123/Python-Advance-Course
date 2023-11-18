rows = int(input())

result = []
matrix = []
result1 = []

for _ in range(rows):                               # cycle fot making the matrix
    # result.extend(int(x) for x in input().split(', '))  # one line result with for cycle

    row = [int(x) for x in input().split(', ')]     # split every row from input
    matrix.append(row)                              # add the row into the matrix

[result1.extend(row) for row in matrix]             # make result list like iterate true the matrix


# print(result)
print(result1)
