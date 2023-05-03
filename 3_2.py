numbers = input("Введите три числа: ")
numbers = numbers.split()
num1 = float(numbers[0])
num2 = float(numbers[1])
num3 = float(numbers[2])
average = (num1 + num2 + num3)/3
print(round(average, 3))
