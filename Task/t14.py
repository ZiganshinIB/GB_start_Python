N = int(input("Введите число N: "))
k = 0
while True:
    if 2**k <= N:
        print(k)
        k += 1
    else:
        break
