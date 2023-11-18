from collections import deque

chocolates = deque(int(x) for x in input().split(', '))     # create deque for chocolate
milk_cups = deque(int(x) for x in input().split(', '))      # create deque for milk

shakes_win = False          # win condition if all chocolates are made
shakes = 0                  # count chocolates

while chocolates and milk_cups:     # if there are any chocolates or milk, loop

    if chocolates[-1] == milk_cups[0]:      # if chocolate is equal to milk
        chocolates.pop()                    # remove chocolate item
        milk_cups.popleft()                 # remove milk item
        shakes += 1                         # add one chocolate
        if shakes == 5:                     # check if 5 shakes are made
            shakes_win = True               # win condition trigger
            break                           # break while cycle
    else:
        if milk_cups[0] <= 0:               # if milf is equal or below zero
            milk_cups.popleft()             # remove milk item
            continue                        # go to start of while cycle
        if chocolates[-1] <= 0:             # if chocolate is equal or below zero
            chocolates.pop()                # remove chocolate
            continue                        # go to start of while cycle
        milk_cups.rotate(-1)                # rotate first item of milk to the end of the deque
        chocolates[-1] -= 5                 # decrease chocolate item with 5


if shakes_win:                              # if win condition is triggered
    print(f'Great! You made all the chocolate milkshakes needed!')      # print results
else:
    print(f'Not enough milkshakes.')                                    # print results

if chocolates:                              # if any chocolate left
    print(f'Chocolate: {", ".join(str(x) for x in chocolates)}')        # print results
else:
    print(f'Chocolate: empty')                                          # print results

if milk_cups:                               # if any milk left
    print(f'Milk: {", ".join(str(x) for x in milk_cups)}')              # print results
else:
    print(f'Milk: empty')                                               # print results
