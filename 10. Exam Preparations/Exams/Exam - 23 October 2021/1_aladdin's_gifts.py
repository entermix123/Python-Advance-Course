materials = list(reversed([int(x) for x in input().split()]))
magic = [int(x) for x in input().split()]
win = False

gifts = {
    'Gemstone': [100, 199],
    'Porcelain Sculpture': [200, 299],
    'Gold': [300, 399],
    'Diamond Jewellery': [400, 499],
}

made = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0,
}

while materials and magic:

    current_material = materials.pop(0)
    current_magic = magic.pop(0)

    present_value = current_material + current_magic

    if present_value < 100:
        if present_value % 2 == 0:
            current_material *= 2
            current_magic *= 3
            present_value = current_material + current_magic

        elif present_value % 2 != 0:
            present_value *= 2

    elif present_value > 499:
        present_value /= 2

    for key, value in gifts.items():
        if value[0] <= present_value <= value[1]:
            made[key] += 1
            break

    if (made['Gemstone'] > 0 and made['Porcelain Sculpture'] > 0) or\
            (made['Gold'] > 0 and made['Diamond Jewellery']) > 0:
        win = True

if win:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

result = ['Materials left: ']
vals = []
if materials:
    for x in materials:
        vals.append(str(x))
    result.append(', '.join(vals))
    print(''.join(result))

result2 = ['Magic left: ']
vals2 = []
if magic:
    for x in magic:
        vals.append(str(x))
    result2.append(', '.join(vals))
    print(''.join(result2))

made = sorted(made.items(), key=lambda x: x[0])

for x, y in made:
    if y > 0:
        print(f'{x}: {y}')
