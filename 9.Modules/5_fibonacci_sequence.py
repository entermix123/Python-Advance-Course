sequence_nums = []


def create_seq(num):
    sequence_nums.clear()
    sequence_nums.append(0)
    sequence_nums.append(1)

    for _ in range(num - 2):
        sequence_nums.append(sequence_nums[-1] + sequence_nums[-2])

    return ' '.join(map(str, sequence_nums))


def locate_num(el):
    if el in sequence_nums:
        el_idx = sequence_nums.index(el)
        return f'The number - {el} is at index {el_idx}'
    else:
        return f'The number {el} is not in the sequence'


def fibonacci_seq():
    while True:
        user = input()
        if user == 'Stop':
            break
        elif user.split()[0] == 'Create':
            print(create_seq(int(user.split()[2])))
        elif user.split()[0] == 'Locate':
            print(locate_num(int(user.split()[1])))


fibonacci_seq()
