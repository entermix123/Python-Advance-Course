text = input()

stack = []

for idx in range(len(text)):            # cycle true input
    char = text[idx]                    # find character
    if char == '(':                     # when find open bracket
        stack.append(idx)               # save index in stack list
    elif char == ')':                   # when find close bracket
        last_bracket_idx = stack.pop()                  # take last open bracket idx
        s_expression = text[last_bracket_idx:idx + 1]   # make text from last open bracket to current close bracket
        print(s_expression)                             # print text
