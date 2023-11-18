def func_executor(*funcs_data):

    result = [f'{func.__name__} - {func(*args)}' for func, args in funcs_data]  # comprehension
    return '\n'.join(result)

    # result = []
    # for func, args in funcs_data:
    #     result.append(f'{func.__name__} - {func(*args)}')
    # return '\n'.join(result)


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor( (make_upper, ("Python", "softUni")), (make_lower, ("PyThOn",)), ))


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor( (sum_numbers, (1, 2)), (multiply_numbers, (2, 4)) ))
