'''
Определить индексы элементов массива (списка), значения
которых принадлежат заданному диапазону (т.е. не меньше 
заданного минимума и не больше заданного максимума).
На вход подается список с элементами list_1 и границы 
диапазона в виде чисел min_number, max_number.
Input:
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

Output:
1
2
3
6
7
9
10
11
13
14
16
19
'''


list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

list_length = len(list_1)

for i in range(list_length):
    value = list_1[i]
    if min_number <= value <= max_number:
        print(i)

#  Better way
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

# Используем enumerate для получения и индекса, и значения элемента списка
for index, value in enumerate(list_1):
    if min_number <= value <= max_number:
        print(index)
