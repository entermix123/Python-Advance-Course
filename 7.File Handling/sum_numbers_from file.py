def sum_nums_from_file(file_name):      # def of function for reading file line by line
    data = open(file_name, 'r')     # make variable and open file_name to read
    sum_nums = 0

    for num in data:               # iterate true file and take line
        sum_nums += int(num)

    return sum_nums


result = sum_nums_from_file('text.txt')     # crate result var and call function for path and file name
print(result)                               # print result
