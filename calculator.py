num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
op = input('Enter Operator: ')

if op == '+':
    print('Addition:', num1 +num2)
elif op == '-':
    print('Subtraction:', num1-num2)
elif op == '*':
    print('Multiplication:', num1*num2)
elif op == '/':
    print('Division:', abs(num1/num2))
else:
    print('Invalid operator')