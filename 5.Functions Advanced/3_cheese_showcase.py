def sorting_cheeses(**kwargs):
    data = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))     # sort by length of elements in list
    result = []                                                         # make result list
    for name, quantity in data:                                         # iterate true sorted data
        result.append(name)                                             # append name
        result.extend(sorted(quantity, reverse=True))                   # extend quantity

    return '\n'.join([str(el) for el in result])                        # on new row return elements of result list


print(sorting_cheeses(Parmesan=[102, 120, 135], Camembert=[100, 100, 105, 500, 430], Mozzarella=[50, 125], ))
