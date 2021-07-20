def add(a, b):
    return float(a) + float(b)


def sub(a, b):
    return float(a) - float(b)


def multi(a, b):
    return float(a) - float(b)


def division(a, b):
    return float(a) / float(b)


num1 = float(input('Enter First Number:'))
num2 = float(input('Enter Second Number:'))
operator = input('Enter the Operator:')
if operator == '+':
    print('Sum of {} and {} = {}'.format(num1, num2, add(num1, num2)))
elif operator == '-':
    print('Subtraction of {} by {} = {}'.format(num1, num2, sub(num1, num2)))
elif operator == '*':
    print('Multiplication of {} with {} = {}'.format(num1, num2, multi(num1, num2)))
elif operator == '/':
    print('Division of {} by {} = {}'.format(num1, num2, division(num1,num2)))2
else:
    print('Invalid Input')
