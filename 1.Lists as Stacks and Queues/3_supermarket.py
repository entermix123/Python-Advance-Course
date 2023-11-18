from collections import deque

people = deque()
while True:
    line = input()

    if line == 'End':
        break

    if line == 'Paid':          # if line is 'Paid'
        # print('\n'.join(people))  # print people on separate line
        for person in people:       # cycle people list
            print(person)           # print every element of the list
        people.clear()              # clear the list
    else:
        people.append(line)         # add line to the list

print(f'{len(people)} people remaining.')   # print how many elements are in the list people
