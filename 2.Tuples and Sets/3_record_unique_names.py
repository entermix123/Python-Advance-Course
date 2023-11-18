names_num = int(input())        # input number of names

names = []                      # make list

for _ in range(names_num):      

    name = input()              # input name

    if name not in names:       # if name not in list
        names.append(name)      # add name to list

    final_names = tuple(names)  # make tuple of the list

for name1 in final_names:       # iterate the tuple
    print(name1)                # print result
