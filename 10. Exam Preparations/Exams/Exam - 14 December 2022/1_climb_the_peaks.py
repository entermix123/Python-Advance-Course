food = list(reversed([int(x) for x in input().split(', ')]))
stamina = [int(x) for x in input().split(', ')]
all_taken = False

peaks = [['Vihren', 80], ['Kutelo', 90], ['Banski Suhodol', 100], ['Polezhan', 60], ['Kamenitza', 70]]
taken = []
days = 0
while True:

    if not peaks:
        all_taken = True
        break

    if not food or not stamina or days > 7:
        break

    days += 1

    day_food = food.pop(0)
    day_stamina = stamina.pop(0)

    energy = day_food + day_stamina
    current_peak = peaks[0][1]
    if energy >= current_peak:
        taken.append(peaks[0][0])
        peaks.pop(0)

if all_taken:
    print(f'Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
else:
    print(f'Alex failed! He has to organize his journey better next time -> @PIRINWINS')

if taken:
    print('Conquered peaks:')
    for x in taken:
        print(x)
