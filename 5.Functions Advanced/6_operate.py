def operate(operator, *args):
    result = args[0]
    if operator in ["+", "-"]:
        for num in args[1:]:
            result = eval(f"{result}{operator}{num}")
    else:
        if 0 in args:
            result = 0
        else:
            for num in args[1:]:
                result = eval(f"{result}{operator}{num}")
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
