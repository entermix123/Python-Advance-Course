def sum_neg():
    sum_nums = 0
    for num in nums:
        if num < 0:
            sum_nums += num
    return sum_nums


def sum_pos():
    sum_nums = 0
    for num in nums:
        if num > 0:
            sum_nums += num
    return sum_nums


nums = [int(x) for x in input().split()]

# positives = sum_pos()
# negatives = sum_neg()

positives = sum(n for n in nums if n > 0)
negatives = sum(n for n in nums if n < 0)


def print_res(a, b):
    print(b)
    print(a)

    if a > abs(b):
        print(f'The positives are stronger than the negatives')
    else:
        print(f'The negatives are stronger than the positives')


print_res(positives, negatives)


