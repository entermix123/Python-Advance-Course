def math_operations(*nums, **operators):    # create function
    for i in range(len(nums)):              # iterate true every number

        # index of every numer is divided by the numbers of operators (4) and left index is nested operator
        key = list(operators.keys())[i % 4]     # take current key

        if key == 'a':                      # if operator is a
            operators[key] += nums[i]       # add value of the current key to current number
        elif key == 's':                    # if operator is s
            operators[key] -= nums[i]       # subtract value of the current key to current number
        elif key == 'd':                    # if operator is d
            if nums[i] != 0:                # if current number is not zero
                operators[key] /= nums[i]   # divide current number with value of the current key
        elif key == 'm':                    # if operator is m
            operators[key] *= nums[i]       # multiply current number with the value of the current key

    # sort operators with discrete function lambda by:
    # value, descending: '-x[1]'
    # key, ascending: 'x[0]'
    operators = sorted(operators.items(), key=lambda x: (-x[1], x[0]))
    return '\n'.join(f'{k}: {v:.1f}' for k, v in operators)  # return key-value pair of operators dictionary on new row


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
