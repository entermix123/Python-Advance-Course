nums1 = set([int(x) for x in input().split()])      # make set of the first sequence of integers
nums2 = set([int(x) for x in input().split()])      # make set of the second sequence of integers

lines = int(input())
for _ in range(lines):

    user = input().split()

    command = user[0]
    subcommand = user[1]

    if command == 'Add':
        add_sequence = set([int(x) for x in user[2:]])

        if subcommand == 'First':
            for num in add_sequence:
                nums1.add(int(num))

        elif subcommand == 'Second':
            for num in add_sequence:
                nums2.add(int(num))

    elif command == 'Remove':
        remove_sequence = set([int(x) for x in user[2:]])

        if subcommand == 'First':
            for num in remove_sequence:
                nums1.discard(num)

        elif subcommand == 'Second':
            for num in remove_sequence:
                nums2.discard(num)

    elif command == 'Check':
        if nums2.issubset(nums1) or nums2.issubset(nums1):
            print(f'True')
        else:
            print(f'False')

print(', '.join(map(str, sorted(nums1))))
print(', '.join(map(str, sorted(nums2))))
