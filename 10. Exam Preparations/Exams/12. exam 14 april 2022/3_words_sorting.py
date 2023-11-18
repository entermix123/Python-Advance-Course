def words_sorting(*words):
    dict1 = {}              # create di dictionary
    result = []             # create result list
    sum_all = 0             # sum all ascii values of all keys
    for key in words:           # iterate true words in user input
        if key not in dict1:    # if key not in dict
            dict1[key] = 0      # add key to dict with value 0
            sum1 = 0            # sum1 = 0, reset fot every key
            for char in key:        # iterate for every character in key word
                sum1 += ord(char)   # add ascii value to sum of the characters in the word
                dict1[key] = sum1   # set value to the key in the dictionary
            sum_all += sum1         # add ascii sum to sum of all ascii value for each key

    if sum_all % 2 != 0:                                    # if sum of all values in dict1 is odd
        dict1 = sorted(dict1.items(), key=lambda x: -x[1])  # sort dictionary by value descending
    else:                                                   # if sum of all values in dict1 is even
        dict1 = sorted(dict1.items(), key=lambda x: x[0])   # sort dictionary by key ascending

    for key, value in dict1:                    # iterate true list of sorted dict1
        result.append(f'{key} - {value}')       # add values to result

    return '\n'.join(result)                    # return values from the result separated by new lines


# print(words_sorting('escape', 'charm', 'mythology'))
# print(words_sorting('escape', 'charm', 'eye'))
print(words_sorting('cacophony', 'accolade'))
