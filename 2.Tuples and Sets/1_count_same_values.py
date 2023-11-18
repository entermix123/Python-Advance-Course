user = tuple(float(x) for x in input().split())
unique = []

for num in user:
    if num not in unique:
        unique.append(num)

for x in unique:
    print(f'{x:.1f} - {user.count(x)} times')
