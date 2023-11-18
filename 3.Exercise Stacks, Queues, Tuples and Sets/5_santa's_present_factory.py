from collections import deque

crafts = deque(int(x) for x in input().split())             # make deque of materials from input
magic_level = deque(int(x) for x in input().split())        # make deque of magic level from input
items = {'Doll': 150, 'Wooden train': 250, 'Teddy bear': 300, 'Bicycle': 400}   # toy dictionary
crafted = {}        # create crafted dictionary
done = False    # condition if presents are crafted

while crafts and magic_level:       # while there are materials and magic levels

    zero_case = False               # zero case condition

    material = crafts[-1]           # find material
    level = magic_level[0]          # find magic level

    if material == 0:               # if material is zero case
        crafts.pop()                # remove material from deque
        zero_case = True            # trigger zero case condition

    if level == 0:                  # if magic level is zero case
        magic_level.popleft()       # remove magic level from deque
        zero_case = True            # trigger zero case condition

    if zero_case:                   # if zero case triggered
        continue                    # start while cycle again

    result = material * level       # find multiplication result

    if result > 0:                          # if result positive number
        for key, value in items.items():    # iterate true toy items
            if result == value:             # if result is equal to one of the toys points
                if key in crafted.keys():   # if toy is in crafted dictionary
                    crafted[key] += 1       # add point to count the crafted toy with same name
                    crafts.pop()            # remove material from deque
                    magic_level.popleft()   # remove magic level from deque
                    break                   # break for cycle
                else:                       # if toy not in crafted dictionary
                    crafted[key] = 1        # add pair toy_name: 1 to crafted dictionary
                    crafts.pop()            # remove material from deque
                    magic_level.popleft()   # remove magic level from deque
                    break                   # break for cycle

        else:                               # if result not in values in toy dictionary
            magic_level.popleft()           # remove magic level from deque
            crafts[-1] += 15                # add 15 points to last value of material in deque

    elif result < 0:                        # if result is negative value
        crafts.append(crafts.pop() + magic_level.popleft())     # add sum of material value and magic level to last material in deque

# if pairs of two toy names in crafted dictionary
if ('Doll' in crafted and 'Wooden train' in crafted) or ('Teddy bear' in crafted and 'Bicycle' in crafted):
    done = True     # trigger done

if done:        # id done triggered
    print(f'The presents are crafted! Merry Christmas!')    # print result
else:
    print(f'No presents this Christmas!')

if crafts:      # if there are items in materials deque
    print(f'Materials left: {", ".join(str(x) for x in reversed(crafts))}')     # iterate true reversed materials deque and print

if magic_level:  # if there are magic levels in deque
    print(f'Magic left: {", ".join(str(x) for x in magic_level)}')       # print magic levels in deque

for key, value in sorted(crafted.items()):  # iterate true sorted crafted dictionary
    print(f'{key}: {value}')                # print crafted toy and count of the toy
