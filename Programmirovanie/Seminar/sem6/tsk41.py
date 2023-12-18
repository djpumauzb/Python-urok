'''
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве  
Далее записаны N чисел — элементы массива. 
Массив состоит из целых чисел. 

Input: 
5
1 2 3 4 5
Output: 0

Input:
5
1 5 1 5 1
Output: 2

'''
def arr(n):
    list_n = []
    for i in range(n):
        list_n.append(int(input("введите элемент массива: ")))
    return list_n

def digit_number(input_list):
    count = 0
    for idx in range(1, len(input_list)-1):
        if input_list[idx] > input_list[idx-1] and input_list[idx] > input_list[idx+1]:
            count += 1
    return count

def main():
    # n = int(input("введите количество элементов первого массива: "))
    # list1 = arr(n)
    list1 = [1, 5, 1, 5, 1, 1, 5, 1, 5, 1, 1, 5, 1, 5, 1, 1, 5, 1, 5, 1]
    print(list1)
    print(digit_number(list1))


main()
