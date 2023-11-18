from collections import deque

people = deque()

all_liters = int(input())       # liters of dispenser

line = input()
while line != "Start":
    people.append(line)         # while people start taking water, add people to list
    line = input()

line = input().split()
while line[0] != 'End':

    if len(line) > 1:           # refill command
        liters = int(line[1])   # what is the amount that is refilled
        all_liters += liters    # add amount to dispenser
    else:
        liters = int(line[0])               # how many liters person will take
        person = people.popleft()           # who is the person
        if liters > all_liters:             # if there is not enough water in the dispenser
            print(f'{person} must wait')    # print result
        else:
            all_liters -= liters            # if there is enough water subtract the amount the person is taking
            print(f"{person} got water")    # print result
    line = input().split()                  # next person

print(f'{all_liters} liters left')          # print result
