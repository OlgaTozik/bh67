n = int(input("введите число: "))
m = int(input("введите число: "))
k = int(input("введите число: "))
counter = 0
i = 0
while counter < n:
    while i % m == 0 and i > k:
        print(i)
        i += 1
        counter += 1
    else:
        i += 1
