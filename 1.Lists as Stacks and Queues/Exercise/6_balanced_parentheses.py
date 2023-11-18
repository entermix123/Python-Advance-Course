from collections import deque

parents = input()
que = deque(x for x in parents)
balabnced = True

while que:
    if que[0] == '{':
        if que[1] == '}':
            que.popleft()
            que.popleft()
        elif que[-1] == '}':
            que.popleft()
            que.pop()
        else:
            balabnced = False
            break
    elif que[0] == '[':
        if que[1] == ']':
            que.popleft()
            que.popleft()
        elif que[-1] == ']':
            que.popleft()
            que.pop()
        else:
            balabnced = False
            break
    elif que[0] == '(':
        if que[1] == ')':
            que.popleft()
            que.popleft()
        elif que[-1] == ')':
            que.popleft()
            que.pop()
        else:
            balabnced = False
            break
    else:
        balabnced = False
        break

print('YES' if balabnced else 'NO')
