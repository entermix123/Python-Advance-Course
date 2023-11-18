text = [x for x in input()]

chars = {}      # create dictionary

for x in text:

    if x not in chars:                # condition for unique char
        occurrences = text.count(x)   # find occurrencesof of the character in the text
        chars[x] = occurrences        # ad char and occurrences to the dictionary

chars1 = sorted(chars.items(), key=lambda x: x[0])  # create list of tuples from sorted dictionary by ascending key

for x, y in chars1:                                 # iterate true list of tuples
    print(f'{x}: {y} time/s')                       # print two objects in every typle
