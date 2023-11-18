SIZE = 6

matrix = []
positions = []
scores = 0
won = False
price = ''

for row in range(SIZE):
    line = input().split()
    # for index, value in enumerate(line):
    #     if value == 'B':
    #         positions.append([row, index])
    for x in line:
        if x.isalpha():
            positions.append([row, line.index(x)])

    matrix.append(line)

prices = {
    'Football': [100, 199],
    'Teddy Bear': [200, 299],
    'Lego Construction Set': [201, 300],
}

for _ in range(3):

    line1 = input().split(', ')
    row = int(line1[0].split('(')[1])
    col = int(line1[1].split(')')[0])
    sum1 = 0

    if [row, col] in positions:
        positions.remove([row, col])
        for x in range(SIZE):
            value = matrix[x][col]
            if value.isdigit():
                scores += int(value)


for key in prices.keys():
    if prices[key][0] <= scores <= prices[key][1]:
        price = key
        won = True

if won:
    print(f"Good job! You scored {scores} points, and you've won {price}.")
else:
    print(f"Sorry! You need {100 - scores} points more to win a prize.")


