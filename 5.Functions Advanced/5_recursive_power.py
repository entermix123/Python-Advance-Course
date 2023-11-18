def recursive_power(n, p):
    if p == 0:
        return 1
    if p == 1:
        return n

    return n * recursive_power(n, p-1)


print(recursive_power(2, 10))
print(recursive_power(10, 100))

# def recur_factorial(n):     # definition of the function
#     if n <= 1:              # if recursion number is 1
#         return n
#
#     result1 = n * recur_factorial(n - 1)            # result for every multiplier
#     print(f'recur_factorial({n}) = {result1}')      # print recursive multiplier and its current result
#
#     return result1                                  # return the result of the current multiplier
#
#
# print(recur_factorial(5))                           # print result of the function
