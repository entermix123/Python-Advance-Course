SIZE = int(input())

directions = [x for x in input().split(', ')]

field = []
current_position = []

for row in range(SIZE):     # iterate true size of the field
    line = list(input())    # save list of input
    if 's' in line:         # check for squirrel start position
        current_position = [row, line.index('s')]   # save start position

    field.append(line)      # append line to field

field[current_position[0]][current_position[1]] = '*'   # make start position '*'

moves = {           # moves coordination
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

die = False     # die condition
collected = 0   # collected nuts

while directions:

    current_move = directions.pop(0)
    current_position[0] = current_position[0] + moves[current_move][0]      # change current position row
    current_position[1] = current_position[1] + moves[current_move][1]      # change current position col

    # if out of range
    if current_position[0] >= SIZE or current_position[0] < 0 or\
            current_position[1] >= SIZE or current_position[1] < 0:
        print(f"The squirrel is out of the field.")
        die = True
        break

    # if step on trap
    if field[current_position[0]][current_position[1]] == 't':
        print(f"Unfortunately, the squirrel stepped on a trap...")
        die = True
        break

    # if step on nut
    if field[current_position[0]][current_position[1]] == 'h':
        collected += 1
        field[current_position[0]][current_position[1]] = '*'

    # if collect 3 nuts
    if collected == 3:
        print(f'Good job! You have collected all hazelnuts!')
        break

if not die and collected < 3:
    print(f'There are more hazelnuts to collect.')

print(f'Hazelnuts collected: {collected}')
