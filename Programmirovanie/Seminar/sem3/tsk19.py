'''
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо,
K – положительное число.

Input: [1, 2, 3, 4, 5] k = 3O
utput: [4, 5, 1, 2, 3]


'''
a = [1, 2, 3, 4, 5]
k = 3
s = 0
while s < k:
    t = a.pop(0)
    a.append(t)
    s += 1
print(a)


# BOLEE MOSHNOE RESHENIE: PROIZVODTELNOST
a = [1, 2, 3, 4, 5]
k = 3
print(a[k:] + a[:k])