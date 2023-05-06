n=int(input('Введите число: '))
c=0
i=0
for i in range (n):
        while i % 2 == 0 and i>=2:
            c = c + 1
            if c % 5 == 0:
                print(i)
            else:
                print(i,end=' ')
            i = i + 1






