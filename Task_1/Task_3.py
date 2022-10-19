num = int(input('Введите число для приобразоания: '))
lst = []
rest = 0
while num > 0:
    rest = num // 2 + num % 2
    if num % 2 == 0:
        lst.append(0)
    else:
        lst.append(1)
    num -= rest
lst.reverse()
print(*lst, sep = '')