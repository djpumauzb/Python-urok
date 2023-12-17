'''
Дан список чисел. Определите, сколько в нем
встречается различных чисел.

Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
'''
k = [1, 1, 2, 0, -1, 3, 4, 4]
j = []


for i in k:
    if i not in j:
        j.append(i)
print(len(j))

# other way without variable with []: 

count = 0
for i in range(len(k)):
    if k[i] not in k[:i]:
        count += 1

# + ekonomiya pamyati xoroshiy kod :)))))))) top way dlya uniikalnix:  set() to'plam unique qberadi:
print(len(set(k)))