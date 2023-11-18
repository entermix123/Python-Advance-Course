from collections import deque

colors = deque(input().split())
mains = ('red', 'yellow', 'blue')
secondary = ('orange', 'purple', 'green')

first_str = ''
last_str = ''
sub_s = ''
sub_s2 = ''
end_color = deque()

while colors:
    if len(colors) > 1:
        first_str = colors.popleft()
        last_str = colors.pop()
        sub_s = first_str + last_str
        sub_s2 = last_str + first_str

        if sub_s in mains or sub_s in secondary:
            end_color.append(sub_s)
        elif sub_s2 in mains or sub_s2 in secondary:
            end_color.append(sub_s2)
        else:
            first_strip, last_strip = first_str[:-1], last_str[:-1]

            if first_strip:
                colors.insert(len(colors) // 2, first_strip)

            if last_strip:
                colors.insert(len(colors) // 2, last_strip)
    else:
        sub_s = colors.popleft()
        if sub_s in mains or sub_s in secondary:
            end_color.append(sub_s)

for idx in range(len(end_color)):
    if end_color[0] == 'orange':
        if 'red' not in end_color or 'yellow' not in end_color:
            end_color.popleft()
        else:
            end_color.append(end_color.popleft())
    elif end_color[0] == 'purple':
        if 'red' not in end_color or 'blue' not in end_color:
            end_color.popleft()
        else:
            end_color.append(end_color.popleft())
    elif end_color[0] == 'green':
        if 'yellow' not in end_color or 'blue' not in end_color:
            end_color.popleft()
        else:
            end_color.append(end_color.popleft())
    else:
        end_color.append(end_color.popleft())

print(list(end_color))
