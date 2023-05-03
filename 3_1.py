sentense = input("Введите предложение: ")

numbreplace = sentense.count(' ')
sentence = sentense.replace(' ', '-', numbreplace)
print(sentence)

s = sentence.split(' ')
sentence = f"{'-'.join(s)}"
print(sentence)
