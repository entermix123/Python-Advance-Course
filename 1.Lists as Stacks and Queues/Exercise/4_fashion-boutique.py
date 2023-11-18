clothes = [int(x) for x in input().split()]

rack = int(input())
count_racks = 1
stack = clothes

sum_values = 0

while clothes:

    if sum_values + clothes[-1] > rack:
        sum_values = clothes.pop()
        count_racks += 1
    elif sum_values + clothes[-1] == rack:
        sum_values = 0
        clothes.pop()
        if clothes:
            count_racks += 1
    else:
        sum_values += clothes.pop()

print(count_racks)
