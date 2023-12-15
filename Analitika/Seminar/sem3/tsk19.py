'''
Dana posledovatelnost' iz N celix chisel i chislo K.
Neobxodimo sdvignut' vsyu posledovatelnost'
(svig - siklicheskiy) na K elementov vpravo, 
K - polojitelnoe chislo.

Input: [1, 2, 3, 4, 5] k = 3

Output: [3, 4, 5, 1, 2]
'''
list1 = [1, 2, 3, 4, 5, -10]
k = int(input('Vvedite K: '))

k = k % len(list1)

list_res = []

for i in range(k):
    list_res.append(list1[len(list1) - 1 - i])
print(list_res)

for i in range(len(list1) - k):
    list_res.append(list1[i])
print(list_res)
