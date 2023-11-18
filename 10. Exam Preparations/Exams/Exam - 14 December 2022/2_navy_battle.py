# def make_move(cur_pos, new_pos):

SIZE = int(input())

field = []
position = []

for row in range(SIZE):
    line = list(input())
    if 'S' in line:
        position = [row, line.index('S')]

    field.append(line)

field[position[0]][position[1]] = '-'

cruisers = 0
hits = 0

moves = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

command = input()
while True:

    position[0] = position[0] + moves[command][0]
    position[1] = position[1] + moves[command][1]

    if field[position[0]][position[1]] == '*':
        field[position[0]][position[1]] = '-'
        hits += 1
        if hits == 3:
            field[position[0]][position[1]] = 'S'
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{position[0]}, {position[1]}]!")
            break

    if field[position[0]][position[1]] == 'C':
        field[position[0]][position[1]] = '-'
        cruisers += 1
        if cruisers == 3:
            field[position[0]][position[1]] = 'S'
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

    command = input()

result = []
for row in field:
    line = ''.join(x for x in row)
    result.append(line)

print('\n'.join(result))
