word = input('Введите слово: ')
dictionary ={symbol:word.count(symbol) for symbol in word}
print(dictionary)

