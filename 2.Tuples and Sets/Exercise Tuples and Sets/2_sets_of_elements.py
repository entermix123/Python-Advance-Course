nums = [int(x) for x in input().split()]

first_set = set()
second_set = set()

for x in range(nums[0]):
    num = input()
    first_set.add(num)

for y in range(nums[1]):
    num = input()
    second_set.add(num)

first_set = first_set.intersection(second_set)
for f in first_set:
    print(f)

