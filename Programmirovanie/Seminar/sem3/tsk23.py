'''
Задача No 23. Общее обсуждениеДан массив, состоящий из целых чисел.
Напишитепрограмму, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)

Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
'''
list1 = [0, -1, 5, 2, 3]
count = 0

for i in range(len(list1)):
    if list1[i-1] < list1[i]:
        count += 1
print(count)

# metod ne s 0 s 1:
count = 0

for i in range(1, len(list1)):
    if list1[i - 1] < list1[i]:
        count += 1
print(count)
