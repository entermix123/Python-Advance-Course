rows, cols = input().split(',')
rows = int(rows)
cols = int(cols)

matrix = []
position = [[], []]
next_position = [[], []]
col = []
cheese = 0

for row in range(rows):
    line = input()
    col = []
    for h in line:
        if h == 'M':
            position = [row, line.index('M')]
        if h == 'C':
            cheese += 1
        col.append(h)

    matrix.append(col)

matrix[position[0]][position[1]] = '*'

moves = {           # moves coordination
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

move = input()
while True:

    if move == 'danger':
        matrix[position[0]][position[1]] = '*'
        print(f"Mouse will come back later!")
        break

    next_position[0] = position[0] + moves[move][0]
    next_position[1] = position[1] + moves[move][1]

    if next_position[0] < 0 or next_position[0] > rows - 1 or next_position[1] < 0 or next_position[1] > cols - 1:
        matrix[position[0]][position[1]] = 'M'
        print(f'No more cheese for tonight!')
        break

    elif matrix[next_position[0]][next_position[1]] == 'T':
        matrix[next_position[0]][next_position[1]] = 'M'
        print(f'Mouse is trapped!')
        break

    elif matrix[next_position[0]][next_position[1]] == 'C':
        matrix[next_position[0]][next_position[1]] = '*'
        position[0] = next_position[0]
        position[1] = next_position[1]
        cheese -= 1

        if cheese == 0:
            matrix[position[0]][position[1]] = 'M'
            print(f'Happy mouse! All the cheese is eaten, good night!')
            break

    elif matrix[next_position[0]][next_position[1]] == '@':
        pass

    elif matrix[next_position[0]][next_position[1]] == '*':
        position[0] = next_position[0]
        position[1] = next_position[1]

    move = input()

for x in matrix:
    print(''.join(x))
