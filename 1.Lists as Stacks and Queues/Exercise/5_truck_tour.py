from collections import deque

all_pumps = int(input())

que = deque()
tank = 0
stops = 0

for pumps in range(all_pumps):
    que.append([int(x) for x in input().split()])   # make deque of the elements

original_que = que.copy()                           # make copy of the original input
while que:
    if stops == len(original_que):                  # if the for cycle goes true all pumps
        start = que[0]                              # find start position of the last que
        start_position = original_que.index(start)  # find start position in the original input
        print(start_position)                       # print result
        break

    for position in range(all_pumps):               # for start position in current que
        liters = que[position][0]                   # find liters petrol
        kilometers = que[position][1]               # find kilometers to next pump
        tank += liters                              # add liters to the tank
        if tank >= kilometers:                      # if in tank has enough petrol
            tank -= kilometers                      # subtract this much liters from tank
            stops += 1                              # passed to the next pump
        else:                                       # if tank has not enough petrol
            rotate = que.popleft()                  # remove current pump from the start of the que
            que.append(rotate)                      # add current pump last in the que
            stops = 0                               # reset stops
            tank = 0                                # reset tank
            break                                   # exit the for cycle

