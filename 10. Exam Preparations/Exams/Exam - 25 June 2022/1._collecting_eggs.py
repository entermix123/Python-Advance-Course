from collections import deque

box_size = 50
boxes = 0

# input
# 20, 13, -7, 7
# 10, 5, 20, 15, 7, 9

eggs = deque()
papers = deque()
start_eggs = input().split(', ')
start_papers = input().split(', ')

[eggs.append(int(x)) for x in start_eggs if int(x)]
[papers.appendleft(int(x)) for x in start_papers]

while eggs and papers:

    current_egg = eggs.popleft()

    if current_egg < 0:
        continue

    if current_egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    current_paper = papers.popleft()

    if current_egg + current_paper <= box_size:
        boxes += 1


papers.reverse()
if boxes >= 1:
    print(f'Great! You filled {boxes} boxes.')
else:
    print(f"Sorry! You couldn't fill any boxes!")
if eggs:
    print(f'Eggs left: {", ".join(str(x) for x in eggs)}')
if papers:
    print(f'Pieces of paper left: {", ".join(str(x) for x in papers)}')
