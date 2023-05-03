name = input('Введите имя: ')
age = input('Введите возраст: ')
town = input('Введите город: ')

print('Добрый день', name, age, town)

print("Добрый день %s %s %s" % (name, age, town))

print(f"Добрый день {name} {age} {town}")