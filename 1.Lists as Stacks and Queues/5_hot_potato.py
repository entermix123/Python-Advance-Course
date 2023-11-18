from collections import deque

children = deque(input().split())
n = int(input())

count = 1
while len(children) > 1:
    child = children.popleft()      # first child
    if count == n:                  # if child is second
        print(f'Removed {child}')   # child removed
        count = 1                   # count child reset
    else:
        count += 1                  # if child is not second
        children.append(child)      # add child to the list

last_child = children.popleft()     # find last child
print(f'Last is {last_child}')      # print last child
