lines = int(input())
unique = set()
for _ in range(lines):

    chemical = [str(x) for x in input().split()]

    for x in chemical:
        unique.add(x)

for k in unique:
    print(k)
