coms = int(input())
db = []
for _ in range(coms):
    line = input().split(', ')
    command = line[0]
    car_num = line[1]

    if command == 'IN':
        if car_num not in db:
            db.append(car_num)

    elif command == 'OUT':
        if car_num in db:
            db.remove(car_num)

if not db:
    print(f'Parking Lot is Empty')
else:
    print('\n'.join(x for x in db))

