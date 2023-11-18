from collections import deque

matrix = [[x for x in input().split()] for x in range(6)]
start_position = []
for row in range(6):
    for col in range(len(matrix)):
        if matrix[row][col] == 'E':
            start_position.append(row)
            start_position.append(col)
            break

water_deposit = 0
metal_deposit = 0
concrete_deposit = 0
resources = False
broken = False
commands = deque(x for x in input().split(', '))
row, col = start_position

while commands and not broken:

    current_command = commands.popleft()

    if current_command == 'up':
        row -= 1
        if row < 0:
            row = 5

    elif current_command == 'down':
        row += 1
        if row > 5:
            row = 0

    elif current_command == 'left':
        col -= 1
        if col < 0:
            col = 5

    else:
        col += 1
        if col > 5:
            col = 0

    if matrix[row][col] == 'W':
        water_deposit += 1
        print(f"Water deposit found at ({row}, {col})")

    elif matrix[row][col] == 'M':
        print(f"Metal deposit found at ({row}, {col})")
        metal_deposit += 1

    elif matrix[row][col] == 'C':
        print(f"Concrete deposit found at ({row}, {col})")
        concrete_deposit += 1

    elif matrix[row][col] == 'R':
        print(f"Rover got broken at ({row}, {col})")
        broken = True
        break

    if water_deposit > 0 and metal_deposit > 0 and concrete_deposit > 0:
        resources = True

if resources:
    print(f"Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")
