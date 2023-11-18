# numbers_list = [int(x) for x in input().split(", ")]
# result = 1
#
# for i in range(len(numbers_list)):
#     number = numbers_list[i]
#     if number <= 5:
#         result *= number
#     elif 5 < number <= 10:
#         result /= number
# print(result)
#
# def sum_odd_even_numbers(nums):
#     even_nums = 0
#
#     for num in nums:
#         if num % 2 == 0 and num != 0:
#             even_nums += num
#         elif type(num) != int:
#             raise TypeError('--Invalid_Data_Type--')        # set TypeError custom text
#         elif num == 0:
#             raise ArithmeticError('Invalid operation by 0')     # set ArithmeticError custom text
#     print(even_nums)
#
#
# try:                                        # try with function sum_odd_even_numbers() with input [3, 5, 6, 0]
#     sum_odd_even_numbers([3, 5, 6, 0])
#
# except TypeError as error:                  # set custom text as error object
#     print(f'Exception handled', error)      # print custom text and custom text form error object
#
# except ArithmeticError as error1:           # set custom text as error object
#     print(f'Exception handled', error1)     # print custom text and custom text form error object

# def hello():                # def function
#     raise AssertionError    # raise error
#
#
# try:                        # try function
#     hello()
#
# except AssertionError as error:     # set exception text as error object
#     print(error)                    # print error
#
# else:                                           # if there is no error
#     try:                                        # nested try
#         with open('file.log') as file:          # open file code
#             read_data = file.read()             # make variable read from file
#     except FileNotFoundError as file_error:     # if file is not found set error as a object
#         print(file_error)                       # print error object
#
# finally:                                        # finally executes with no condition
#     'some code'


# Custom Exception:

# class CustomException(Exception):
#     pass
#
#
# try:
#     raise CustomException('This is my exception')
#
# except CustomException as error:
#     print(error)

# class FahrenheitError(Exception):       # make class for exception error
#     min_f = 32                          # set min value
#     max_f = 212                         # set max value
#
#     def __init__(self, f, *args):       # def start function
#         super().__init__(args)          # use super() function with min and max values
#         self.f = f                      # set user input to main value
#
#     def __str__(self):                  # set print function
#         return f'The {self.f} is not in a valid range {self.min_f, self.max_f}'  # return wanted output
#
#
# def fahrenheit_to_celsius(f: float) -> float:
#     if f < FahrenheitError.min_f or f > FahrenheitError.max_f:      # check if user input is in range
#         raise FahrenheitError(f)                                    # CUSTOM ERROR
#     return (f - 32) * 5 / 9                                         # return value in celsius
#
#
# value = input('Enter a temperature in Fahrenheit: ')                # user input
#
# try:                                                                # try case
#     f = float(value)                                                # make user input float
# except ValueError as error:                                         # make ValueError error object
#     print(error)                                                    # print error
# else:
#     try:                                                            # if no ValueError
#         result = fahrenheit_to_celsius(float(f))             # call function fahrenheit_to_celsius() with user input
#     except FahrenheitError as error:                         # make custom error as error object
#         print(error)                                         # print error object
#     else:
#         print(f'{f} Fahrenheit = {result:.4f} celsius')      # print result if input value in range


