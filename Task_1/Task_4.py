n = int(input('Введите число: '))
fib = []
nega = []
for i in range(n + 1):
    if i == 0:
        fib.append(0)
    elif i == 1:
        fib.append(1)
    else:
        fib.append(fib[i - 1] + fib[1 - 2])
for i in range(n, 0, -1):
    nega.append(((-1) ** (i + 1)) * fib[i])
print('Для k = ', n, end = '--> ')
print(nega + fib)