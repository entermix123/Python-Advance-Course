from math import log        # import logarithmic function from math
number = int(input())
base = input()

if base == 'natural':               # if base is not integer
    print(f'{log(number):.2f}')
else:
    print(f'{log(number, int(base)):.2f}')
