'''
Задача №43. Решение в группах Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые два элемента, равные друг
другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. 
Все числа списка находятся на разных строках.

Input:
1 2 3 2 3

Output:
2
'''
# if __name__ == '__main__': # esli nzvanie fayla rovno na main
#     print(__name__) # __main__
# print(f'old file: {__name__}')

import utils

def count_pair(list_: list[int]):
    count = 0
    for elem in set(list_):
        count += list_.count(elem) // 2  # vernet kolichestvo elementov v znacheniyax
    return count

def main():
    #list1 = utils.arr(5)
    list1 = [1, 2, 3, 2, 3]
    print(count_pair(list1))

if __name__ == '__main__':
    main()