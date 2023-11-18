caffeine = list(reversed([int(x) for x in input().split(', ')]))
energy_drinks = [int(x) for x in input().split(', ')]

max_energy = 300
energy = 0

while caffeine and energy_drinks:

    current_caffeine = caffeine[0]
    current_energy = energy_drinks[0]

    result_energy = current_caffeine * current_energy

    if energy + result_energy <= max_energy:
        caffeine.pop(0)
        energy_drinks.pop(0)
        energy += result_energy

    else:
        caffeine.pop(0)
        energy_drinks.append(energy_drinks.pop(0))
        if energy - 30 >= 0:
            energy -= 30


if energy_drinks:
    print(f'Drinks left: {", ".join(str(x) for x in energy_drinks)}')
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f'Stamat is going to sleep with {energy} mg caffeine.')