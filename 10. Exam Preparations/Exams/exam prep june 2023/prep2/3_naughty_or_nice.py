def naughty_or_nice_list(santa_list, *args, **kwargs):

    nice_kids = []
    naughty_kids = []
    result = []

    def place_kid():
        if len(kids) == 1:  # if ony one kid in kids

            # add kid to nice_kids if Nice, else add it to naughty_kids
            nice_kids.append(kids[0][1]) if type_kid == 'Nice' else naughty_kids.append(kids[0][1])
            santa_list.remove(*kids)
            # nice_kids.extend(kids) if type_kid == 'Nice' else naughty_kids.extend(kids)
            # santa_list.remove(kids[0])

    for kid_data in args:                       # check strings in args
        number, type_kid = kid_data.split('-')  # split number and name in the tuple

        # check if any kid in santa_list have same number. If so add it to kids
        kids = [info for info in santa_list if info[0] == int(number)]
        place_kid()     # call function

    for name, type_kid in kwargs.items():                           # check
        kids = [info for info in santa_list if info[1] == name]
        place_kid()

    if nice_kids:
        result.append(f'Nice: {", ".join(nice_kids)}')
    if naughty_kids:
        result.append(f'Naughty: {", ".join(naughty_kids)}')
    if santa_list:
        result.append(f'Not found: {", ".join(kid[1] for kid in santa_list)}')

    return '\n'.join(result)


print(naughty_or_nice_list([(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy"), ],
"3-Nice", "1-Naughty", Amy="Nice", Katy="Naughty", ))
# print(naughty_or_nice_list( [ (7, "Peter"), (1, "Lilly"), (2, "Peter"), (12, "Peter"), (3, "Simon"), ],
# "3-Nice", "5-Naughty", "2-Nice", "1-Nice", ))
# print(naughty_or_nice_list([(6, "John"), (4, "Karen"), (2, "Tim"), (1, "Merry"), (6, "Frank"), ],
#                            "6-Nice", "5-Naughty", "4-Nice", "3-Naughty", "2-Nice", "1-Naughty",
#                            Frank="Nice", Merry="Nice", John="Naughty", ))