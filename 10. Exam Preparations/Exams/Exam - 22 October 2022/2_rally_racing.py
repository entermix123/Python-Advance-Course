SIZE = int(input())
racing_number = input()

matrix = [[x for x in input().split()] for x in range(SIZE)]
position = [0, 0]
kilometers = 0
tunnels = []

for row in matrix:
    if 'T' in row:
        tunnels.append([matrix.index(row), row.index('T')])

moves = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}


while True:

    command = input()

    if command == 'End':
        matrix[position[0]][position[1]] = 'C'
        print(f'Racing car {racing_number} DNF.')
        break

    position[0] = position[0] + moves[command][0]
    position[1] = position[1] + moves[command][1]

    if matrix[position[0]][position[1]] == '.':
        kilometers += 10

    elif matrix[position[0]][position[1]] == 'T':
        matrix[position[0]][position[1]] = '.'
        tunnels.remove([position[0], position[1]])
        position = tunnels[0]
        kilometers += 30
        matrix[position[0]][position[1]] = '.'

    elif matrix[position[0]][position[1]] == 'F':
        kilometers += 10
        matrix[position[0]][position[1]] = 'C'
        print(f'Racing car {racing_number} finished the stage!')
        break

print(f"Distance covered {kilometers} km.")

final_matrix = [''.join(x) for x in matrix]

for x in final_matrix:
    print(x)
