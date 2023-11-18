lines = int(input())
numbers = []                                                    # make temporary list
final_list = []                                                 # make final list

for _ in range(lines):

        user = input().split('-')                               # split input to first and second range of nums
        first_start, first_end = user[0].split(',')             # split input and take first star and first end nums
        second_start, second_end = user[1].split(',')           # split input and take second start and second end nums

        start_nums = max(int(first_start), int(second_start))   # find maximum start number
        end_nums = min(int(first_end), int(second_end))         # find minimum end number
        numbers = []                                            # clear temporary number list
        for x in range(int(start_nums), int(end_nums) + 1):     # iterate true start and end found numbers as range
            numbers.append(x)                                   # add numbers in range to temporary list

        if len(numbers) > len(final_list):                      # match length of the last longest list with current
            final_list = numbers                                # if current list is longer make him final , longest

print(f'Longest intersection is {final_list} with length {len(final_list)}')        # print result

