from modules import mathematical_operations

try:
    data = mathematical_operations(*input('Enter first number, operator and second number: ').split(' '))
    print(f'Result is: {data:.2f}')
except ValueError:
    print('Enter a valid data!')
