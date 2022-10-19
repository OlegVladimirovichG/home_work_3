from decimal import *
lst = [1.1, 1.2, 3.1, 5.0001, 10.01]
min, max = 1, 0
for element in lst:
    element = str(element)
    element = element.split('.') if '.' in element else ['0', '0']
    fract_part = int(element[1])/10**len(element[1])
    if fract_part > max:
        max = fract_part
    if fract_part < min:
        min = fract_part
print(f'\nMin = {min}, Max = {max}:')
print(f'Разница = {Decimal(str(max)) - Decimal(str(min))}')