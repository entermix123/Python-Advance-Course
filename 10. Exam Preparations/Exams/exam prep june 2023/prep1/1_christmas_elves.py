energy = [int(x) for x in input().split()]
toys = list(reversed([int(x) for x in input().split()]))


sum_energy = 0
toys_made = 0
toy_counter = 0
total_toys_made = 0
double = False
clumsy = False

while energy and toys:

    current_energy = energy.pop(0)
    current_toy = toys[0]

    if current_energy < 5:
        continue

    toy_counter += 1
    toys_made = 0

    if toy_counter % 3 == 0:
        current_toy *= 2
        toys_made += 1

    if current_energy >= current_toy:
        sum_energy += current_toy
        current_energy -= current_toy

        if toy_counter % 5 != 0:
            current_energy += 1
            toys_made += 1
        else:
            toys_made = 0

        toys.pop(0)

    else:
        current_energy *= 2
        toys_made = 0

    total_toys_made += toys_made
    energy.append(current_energy)

print(f"Toys: {total_toys_made}")
print(f"Energy: {sum_energy}")

if energy:
    print(f"Elves left: {', '.join(str(x) for x in energy)}")
if toys:
    print(f"Boxes left: {', '.join(str(x) for x in reversed(toys))}")
