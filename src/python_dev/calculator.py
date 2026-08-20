sign = input(
    "Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ")
num1 = float(input('Enter first number: '))
if sign.lower() == 'f':
    print(f'{num1} Celsius is equivalent to {(num1*9/5)+32} fahrenheit')
else:
    num2 = float(input('Enter second number: '))

    if sign == '+':
        print(f'Answer is: {num1 + num2}')
    elif sign == '-':
        print(f'Answer is: {num1 - num2}')
    elif sign == '*':
        print(f'Answer is: {num1 * num2}')
    elif sign == '/':
        print(f'Answer is: {num1 / num2}')
    else:
        print('Input error!')
