'''
Dan massiv, sostoyashiy iz celnix chisel. Napishite
programmu, kotoraya podschitaet kolichestvo 
elementov massiva, boslhix predidushego (elementa
s predidushim nomerom)

Input: [0, -1, 5, 2, 3]  #(-1 < 5, 2 < 3)
Output: 2 
'''
list1 = [0, -1, 5, 2, 3]
count = 0

for i in range(1, len(list1)):
    if list1[i] > list1[i-1]:
        count += 1
print(count)