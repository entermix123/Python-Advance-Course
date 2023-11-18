lines = int(input())

current_row = 0                 # create current row counter
sum_ASCII = 0                   # create sum_ascii variable int
even_set = set()                # create even set
odd_set = set()                 # create odd set
final_set = set()               # create final set

for _ in range(lines):
    current_row += 1                # add point to each cycle loop
    name = input()                  # name input
    sum_ASCII = 0                   # reset ascii sum
    for char in name:               # iterate true the current name
        sum_ASCII += ord(char)      # sum ascii values to ascii sum variable

    number = sum_ASCII//current_row     # divide sum ascii to cycle loop count and save to number

    if number % 2 != 0:                 # if number is even
        odd_set.add(number)             # add number to even set
    else:
        even_set.add(number)            # if number is odd, add number to odd set

if sum(even_set) == sum(odd_set):                           # if sums of the sets are equal
    final_set = even_set.union(odd_set)                     # create final set with union
    print(f'{", ".join(str(x) for x in final_set)}')        # print result

elif sum(even_set) > sum(odd_set):                          # if sums of the even set is bigger
    final_set = even_set.symmetric_difference(odd_set)      # create final set with symmetric_difference
    print(f'{", ".join(str(x) for x in final_set)}')        # print result

else:                                                       # if sums of the odd set is bigger
    final_set = odd_set.difference(even_set)                # create final set with difference
    print(f'{", ".join(str(x) for x in final_set)}')        # print result
