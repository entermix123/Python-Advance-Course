# def even_odd_filter(**lists):
#     dict1 = {}
#     for key, value in lists.items():
#         if key == 'even':
#             dict1[key] = []
#             for el in value:
#                 if el % 2 == 0:
#                     dict1[key].append(el)
#         if key == 'odd':
#             dict1[key] = []
#             for el in value:
#                 if el % 2 != 0:
#                     dict1[key].append(el)
#
#     return dict1
def even_odd_filter(**numbers):
    dict1 = {}
    if 'odd' in numbers:
        # numbers['odd'] = [n for n in numbers['odd'] if n % 2 == 1]              # comprehension for odd
        numbers['odd'] = list(filter(lambda x: x % 2 == 1, numbers['odd']))

    if 'even' in numbers:
        # numbers['even'] = [n for n in numbers['even'] if n % 2 == 0]          # comprehension for even
        numbers['even'] = list(filter(lambda x: x % 2 == 0, numbers['even']))   # filtering of even numbers with lambda

    return dict(sorted(numbers.items(), key=lambda x: -len(x[1])))              # sorting by value descending


print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2],))
print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5],))
