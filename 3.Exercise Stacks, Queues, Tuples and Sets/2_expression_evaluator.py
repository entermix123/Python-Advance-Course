from functools import reduce        # import reduce --> check reduce() function info!
user = input().split()              # input: 10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *    # result: 164

'''
reduce() is used if in iterable sequence we need to add a sign between every next item. 
Make calculation and continue with next item.
'''

temp = []
chars = ["*", "+", "-", "/"]

for item in user:    # second logic option --> else:

    if item.lstrip('-').isnumeric():            # if item is numeric
        temp.append(int(item))                  # add to temp steck

    else:   # second logic option --> if item in chars          # check operator
        if item == '*':
            temp = [reduce(lambda x, y: x * y, temp)]
        elif item == '-':
            temp = [reduce(lambda x, y: x - y, temp)]
        elif item == '+':
            temp = [reduce(lambda x, y: x + y, temp)]
        elif item == '/':
            temp = [reduce(lambda x, y: x // y, temp)]

print(temp[0])      # print result
