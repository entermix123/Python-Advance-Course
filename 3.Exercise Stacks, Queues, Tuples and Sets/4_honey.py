from collections import deque

working_bees = deque(int(x) for x in input().split())       # make deque for bees
nectar = deque(int(x) for x in input().split())             # make deque for nectar
mathematics = deque(str(x) for x in input().split())        # make deque for mathematical symbols

honey = 0                                                   # make stack for honey

while working_bees and nectar:                              # while there are bees, nectar and symbols, loop

    if nectar[-1] >= working_bees[0]:                       # if nectar is more than the bee value
        symbol = mathematics.popleft()                      # remove mathematical symbol from deque
        col_nectar = nectar.pop()                           # remove nectar from nectar deque
        bee = working_bees.popleft()                        # remove bee from bee deque
        if symbol == '*':
            honey += abs(bee * col_nectar)       # find honey made
        elif symbol == '/':
            if col_nectar == 0 or bee == 0:      # skip divide by 0 case
                continue
            honey += abs(bee / col_nectar)       # find honey made
        elif symbol == '+':
            honey += abs(bee + col_nectar)       # find honey made
        elif symbol == '-':
            honey += abs(bee - col_nectar)       # find honey made

    elif nectar[-1] < working_bees[0]:      # if nectar is smaller than the bee value
        nectar.pop()                        # remove nectar from nectar deque

print(f'Total honey made: {honey}')    # print total honey made

if working_bees:                            # if any bees left
    print(f'Bees left: {", ".join(str(x) for x in working_bees)}')  # print bees
if nectar:                                  # if any nectar left
    print(f'Nectar left: {", ".join(str(x) for x in nectar)}')     # print nectar
