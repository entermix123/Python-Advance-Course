matrix = []

# . . . . . .
# . 6 . . . .
# G . S . t S
# . . 10 . . .
# . 95 . . 8 .
# . . P . . .
# (1, 1)
# Create, down, r
# Update, right, e
# Create, right, a
# Read, right
# Delete, right
# Stop

for i in range(6):
    row_input = list(input().split())
    matrix.append(row_input)
pos = input()
row = int(pos[1])
col = int(pos[4])
line = input()

while line != 'Stop':

    command = line.split(', ')[0]
    direction = line.split(', ')[1]

    if direction == 'up':
        row -= 1
    elif direction == 'down':
        row += 1
    elif direction == 'left':
        col -= 1
    elif direction == 'right':
        col += 1

    if command == "Create":
        value_create = line.split(', ')[2]
        if matrix[row][col] == '.':
            matrix[row][col] = value_create

    elif command == "Update":
        value_update = line.split(', ')[2]
        if matrix[row][col] != '.':
            matrix[row][col] = value_update

    elif command == "Delete":
        if matrix[row][col] != '.':
            matrix[row][col] = '.'

    elif command == "Read":
        if matrix[row][col] != '.':
            print(matrix[row][col])

    line = input()

for mat_line in matrix:
    print(' '.join(mat_line))
