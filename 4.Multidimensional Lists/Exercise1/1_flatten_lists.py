user = input().split('|')       # separate items by '|'

result = []                     # make new list

for char in user[::-1]:            # iterate true reversed user input
    result.extend(char.split())    # add items to, separated by space

print(*result)                     # print every item in result list
