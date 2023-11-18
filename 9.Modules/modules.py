import pyfiglet
import operator as op


def convert_text_to_ascii(text):                # import pyfiglet
    result = pyfiglet.figlet_format(text)
    # result = pyfiglet.figlet_format(text, font='3-d')
    # result = pyfiglet.figlet_format(text, font='5lineoblique')
    return result


def triangle(num):
    figure = ''

    for n in range(1, num+1):
        for i in range(1, n+1):
            figure += f'{i} '
        figure += '\n'

    for n in range(num, 0, -1):
        for i in range(1, n):
            figure += f'{i} '
        figure += '\n'

    return figure


def mathematical_operations(num1, operator, num2):          # import operator as op
    first_number, second_number = float(num1), int(num2)
    vali_operator = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv, '^': op.pow}

    return vali_operator[operator](first_number, second_number)
