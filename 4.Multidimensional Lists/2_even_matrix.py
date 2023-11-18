rows = int(input())

result = []

for _ in range(rows):

    row = [int(x) for x in input().split(', ') if int(x) % 2 == 0]    # pars (int(x)) items 2 times, but iterate matrix one time
    result.append(row)                                                # add list in result list

    # result.append([int(x) for x in input().split(', ') if int(x) % 2 == 0])  # one line comprehension, one iterate, twp pars

print(result)   # print result
