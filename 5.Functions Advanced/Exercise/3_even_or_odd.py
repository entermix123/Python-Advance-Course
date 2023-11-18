def even_odd(*args):                                                # create function
    if args[-1] == 'even':                                          # check if command is 'even'
        return [int(x) for x in args[:-1] if x % 2 == 0]            # take all items without last one - the command
    else:                                                           # if command is 'odd'
        return [int(x) for x in args[:-1] if x % 2 != 0]            # take all items without last one - the command


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
