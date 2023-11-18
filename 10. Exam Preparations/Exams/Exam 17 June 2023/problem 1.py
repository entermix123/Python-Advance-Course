tools = [int(x) for x in input().split()]
substances = list(reversed([int(x) for x in input().split()]))
challenges = [int(x) for x in input().split()]

while substances and tools:

    current_tool = tools.pop(0)
    current_substance = substances.pop(0)

    value = current_substance * current_tool

    if value in challenges:
        challenges.remove(value)
    else:
        current_tool += 1
        tools.append(current_tool)

        current_substance -= 1
        if not current_substance == 0:
            substances.insert(0, current_substance)

    if not challenges:
        break

if challenges:
    print(f'Harry is lost in the temple. Oblivion awaits him.')
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

result_tools = ['Tools: ']
result_tools1 = []
if tools:
    for x in tools:
        result_tools1.append(str(x))
    result_tools.append(', '.join(result_tools1))
    print(''.join(result_tools))

result_substances = ['Substances: ']
result_substances1 = []
if substances:
    for x in substances:
        result_substances1.append(str(x))
    result_substances.append(', '.join(result_substances1))
    print(''.join(result_substances))

result_challenges = ['Challenges: ']
result_challenges1 = []
if challenges:
    for x in challenges:
        result_challenges1.append(str(x))
    result_challenges.append(', '.join(result_challenges1))
    print(''.join(result_challenges))

