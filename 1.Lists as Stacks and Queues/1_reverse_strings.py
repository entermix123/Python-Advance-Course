text = list(input())
result = []

while text:                # when stack in empty, break
    result.append(text.pop())

    # print(text.pop(), end='')     # standard solution

print(''.join(result))
