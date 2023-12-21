'''
Дано натуральное число N и последовательность
из N элементов. Требуется вывести эту 
последовательность вобратном порядке.

Примечание. В программе запрещается
объявлять массивы и использовать 
циклы(даже для ввода и вывода).

Input: 2 -> 3 4
Output: 4 3
'''

def n_seq(n: int):
    k = input('vvedite chislo:\n')
    if n == 1:
        return k
    return n_seq(n-1) + k

f = int(input('vvedetee kol-vo elementov: '))
print(n_seq(f))
