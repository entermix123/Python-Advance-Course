def start_spring(**user):
    objects = {}                        # create dictionary
    result = []                         # create list for result string

    for value, key in user.items():     # swap keys and values from user input and fill dictionary
        if key not in objects:          # if key do not exist in the dictionary
            objects[key] = []           # add key with empty list for value

        objects[key].append(value)      # add value to the existing key

    # SORTING
    # first sort by number of values descending: -len(x[1]
    # second sort by name of values alphabetically: x[0]
    objects = sorted(objects.items(), key=lambda x: (-len(x[1]), x[0]))     # objects is list!!!

    for obj, values in objects:     # iterate true keys and values in sorted list
        result.append(f'{obj}:')     # add key to result string in wanted format

        for value in sorted(values):    # iterate true values for current key
            result.append(f'-{value}')  # add value to result string in wanted format

    return '\n'.join(result)            # return result items separated by new line


example_objects = {"Water Lilly": "flower", "Swifts": "bird", "Callery Pear": "tree", "Swallows": "bird",
                   "Dahlia": "flower", "Tulip": "flower"}
print(start_spring(**example_objects))
