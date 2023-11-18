from collections import deque

plays = deque(input().split(', '))  # players turns

matrix = [[x for x in input().split()] for x in range(6)]  # matrix

end = False
tom_wall = False
jerry_wall = False

while not end:
    player = plays[0]
    row, col = [int(x) for x in input().strip("()").split(", ")]
    if player == 'Tom' and tom_wall:
        plays.rotate(-1)
        tom_wall = False
        continue
    if player == 'Jerry' and jerry_wall:
        plays.rotate(-1)
        jerry_wall = False
        continue
    position = matrix[row][col]
    current_player = player
    if matrix[row][col] == 'E':
        end = True
        print(f"{plays[0]} found the Exit and wins the game!")
        break
    elif matrix[row][col] == 'T':
        end = True
        print(f"{player} is out of the game! The winner is {plays[1]}.")
        break
    elif matrix[row][col] == 'W':
        if plays[0] == 'Tom':
            tom_wall = True
            print(f"{player} hits a wall and needs to rest.")
            plays.rotate(-1)
        else:
            jerry_wall = True
            print(f"{player} hits a wall and needs to rest.")
            plays.rotate(-1)
    else:
        plays.rotate(-1)

# Jerry, Tom
# . . . W . .
# . . T T . .
# . . . . . .
# . T . W . .
# W . . . E .
# . . . W . .
# (0, 3)
# (3, 3)
# (1, 3)
# (2, 2)
# (3, 5)
# (4, 0)
# (5, 3)
# (3, 1)
# (4, 4)
# (4, 4)
