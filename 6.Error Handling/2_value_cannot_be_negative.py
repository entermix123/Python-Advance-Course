# list1 = [1, 4, -5, 3, 10]
#
# try:
#     new_list = []
#     for x in range(len(list1)):
#         if list1[x] <= 0:
#             raise ZeroDivisionError
#         else:
#             new_list.append(x / 2)
#
# except:
#     print('Exception handles')

# def simple_func():
#     raise TypeError
#
#
# try:
#     simple_func()
# except IndexError:
#     print('Index error - Exception handled')
# except TypeError:
#     print('Type error - Exception handled')

class ValueCannotBeNegative(Exception):  # create class custom Exception
    pass


numbers = [int(input()) for _ in range(5)]  # create list of integers of input

for num in numbers:         # iterate true list of integers
    if num < 0:             # if item is negative
        raise ValueCannotBeNegative(f'Value not negative number.Convert {num} to {abs(num)}')   # raise error

