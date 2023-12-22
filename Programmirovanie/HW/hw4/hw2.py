'''
Заполните массив элементами арифметической прогрессии. Её первый элемент a1,
разность d и количество элементов n будет задано автоматически. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

Input:
a1 = 2
d = 3
n = 4

Output:
2
5
8
11
'''

a1 = 2
d = 3
n = 4


def arithmetic_progression(start, step, length):
    count = start
    for _ in range(1, length):
        print(count)
        count += step
        if count == start + (length - 1) * step:
            print(count)

# Better version:


def arithmetic_progression_upgrade(start: int, step: int, length: int) -> int:
    for count in range(start, start + step * length, step):
        print(count)


arithmetic_progression(a1, d, n)
arithmetic_progression_upgrade(a1, d, n)
