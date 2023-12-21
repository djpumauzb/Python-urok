'''
Хацкер Василий получил доступ к классному журналу ихочет заменить все 
свои минимальные оценки намаксимальные. Напишите программу, котораязаменяет
оценки Василия, но наоборот: всемаксимальные – на минимальные.

Input: 5 -> 1 3 3 3 4
Output:  1 3 3 3 1
'''


def hack(list1):
    min_ = min(list1)
    max_ = max(list1)
    for i in range(len(list1)):
        if list1[i] == max_:
            list1[i] = min_
    return list1


def get_list(str_: str):
    list_out = str_.split()
    for i in range(len(list_out)):
        list_out[i] = int(list_out[i])  # pereobrazovanie v int
    print(*list_out)
    return list_out


iptstr = '1 3 3 3 4'
print(*hack(get_list(iptstr)))
