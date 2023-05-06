num1 = int(input('Введите первое число: '))
action = input('Выберите действие(+,-,/,*): ')
num2 = int(input('Введите второе число: '))
result = 0
action = action.lstrip()
if action == '+':
    result = num1+num2
    print(result)
elif action == '-':
    result = num1 - num2
    print(result)
elif action == '/':
    result = num1/num2
    print(result)
else:
    result = num1*num2
    print(result)
