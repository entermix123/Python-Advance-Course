operate_file = 'text.txt'

symbols = ["-", ",", ".", "!", "?"]

with open(operate_file, 'r') as file:       # open file for read only
    text = file.readlines()                 # save content to text variable as a list with items for every row
    print(text)

for row in range(0, len(text), 2):          # iterate true text for every second (even) row

    for symbol in symbols:                              # iterate true symbols for current row
        text[row] = text[row].replace(symbol, "@")      # replace every existing symbol in the row with '@'

    # print(text[row][::-1])      # prints every letter back words !!! Not a solution for the problem.

    # unpack (*) current row, split by words, reverse word arrangement and separate them by space
    print(*text[row].split()[::-1], sep=' ')
