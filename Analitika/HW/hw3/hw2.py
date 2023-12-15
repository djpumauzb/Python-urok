'''
Требуется найти в массиве list_1 самый близкий 
по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. 
Если значение k совпадает с этим элементом - выведите его.

list_1 = [1, 2, 3, 4, 5]
k = 6

# 5
'''
list_1 = [1, 2, 3, 4, 5, 6]
k = 6

# Введите ваше решение ниже

min_diff = float('inf')
result = 0

for i in list_1:
    if k > i:
        diff = k - i
    else:
        diff = i - k
    if diff < min_diff:
        min_diff = diff
        result = i

print(result)

# Method with ternary operator

min_diff = float('inf')
result = 0

for i in list_1:
    diff = k - i if k > i else i - k  # Вычисляем текущую разницу
    if diff < min_diff:
        min_diff = diff
        result = i

print(result)

# Ispolszuem funsiyu abs()

min_diff = float('inf')
result = 0

for i in list_1:
    diff = abs(k-i)
    if diff < min_diff:
        min_diff = diff
        result = i

print(result)