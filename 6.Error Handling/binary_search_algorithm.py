def binary_search(nums, target_value):      # binary search function logic
    left = 0                                # set left index of the list
    right = len(nums) - 1                   # set right index of the list

    while left <= right:                    # if left index is not equal or higher then right index
        middle_index = (left + right) // 2      # divide range from left to right index by 2
        middle_element = nums[middle_index]     # find middle element

        if middle_element == target_value:      # check if middle element is searched value
            return middle_index                 # if it is, return value

        if target_value > middle_element:       # if searched value is grater then middle element
            left = middle_index + 1             # set new left index
        else:                                   # if searched value is lower than middle element
            right = middle_index - 1            # set new right index


nums = [int(x) for x in input().split(', ')]        # make list of user input numbers
target_value = int(input())                         # make integer of input target value
result = binary_search(nums, target_value)   # make result variable by call function binary_search() with user inputs
print(f'Target value index is: {result}')    # print result value index

# input 1, 2, 3, 4, 5
# input 4
# Target value index is: 3
