from collections import deque

programmer = deque(int(x) for x in input().split())
tasks = deque(int(x) for x in input().split())

ducks = {
    'Darth Vader Ducky': [0, 60],
    'Thor Ducky': [61, 120],
    'Big Blue Rubber Ducky': [121, 180],
    'Small Yellow Rubber Ducky': [181, 240]
}
given_ducks = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0
}

while programmer and tasks:

    current_time = programmer.popleft()
    current_task = tasks.pop()

    result_time = current_time * current_task

    for key, value in ducks.items():
        if ducks[key][0] <= result_time <= ducks[key][1]:
            given_ducks[key] += 1
            break
    else:
        tasks.append(current_task - 2)
        programmer.append(current_time)


print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded: ")
for key, value in given_ducks.items():
    print(f'{key}: {value}')
