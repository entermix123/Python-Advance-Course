user = int(input())

stack = []

for _ in range(user):
    line = input().split()
    command = line[0]
    if command == '1':                # if command is '1' and stack is not empty
        stack.append(line[1])         # add line to stack
    elif command == '2' and stack:    # if command is '2' and stack is not empty
        stack.pop()                   # remove the line from stack
    elif command == '3' and stack:    # if stack is '3' and stack is not empty
        print(max(stack))             # print maximum in stack
    else:                             # if command is '4' and stack is not empty
        if stack:
            print(min(stack))         # print minimum in stack
# n = len(stack)                        # take length of the stack
# for idx in range(len(stack)):         # cycle the stack
#     space = ', ' if idx < n - 1 else ''   # ternary operator in python, making space and comma exclude last element
#     print(stack.pop() + space, end ='')   # print result on one line
print(*stack[::-1], sep=', ')
