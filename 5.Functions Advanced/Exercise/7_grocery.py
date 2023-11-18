def grocery_store(**products):

    # comprehension one line --> not readable !
    # return '\n'.join([f'{k}: {v}' for k, v in sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))])

    # comprehension readable
    products = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))    # sorting of products
    return '\n'.join(f'{k}: {v}' for k, v in products)                     # return key, value in products on new row

    # sorting with discrete function lambda by:
    # value, descending: '-x[0]',
    # length of the name, descending: '-len(x[0])',
    # key alphabetically, ascending: 'x[0]'
    # products = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))  # make list of tuples
    # result = []                                                                   # create empty list

    # for product, quantity in products:                                            # iterate true sorted dictionary
    #     result.append(f'{product}: {quantity}')                                   # add items in correct order
    #
    # return '\n'.join(result)                                                      # return items in list on new row


print(grocery_store(bread=5, pasta=12, eggs=12, ))
