'''
V spiske xranitsya chisla. Nujno vibrat' tolko chetnie
chisla i sostavit' spisok par
(sile;kvadrat chisla).

Input: 1 2 3 5 8 15 23 38
Output: [(2,4), (8,64), (38,1444)]
'''

# inpt = input('Vvedite danni dlya spiski: ')
# data =  [int(i) for i in inpt.split()]


# # for i in data:
# #     if i % 2 == 0:
# #         result.append((i, i**2))
# result = [(i, i**2) for i in data if i % 2 == 0] # etot ludshe cham vsverxu

# print(result)

# lambda fuksiya orqali qisqartirish:


data = [1, 2, 3, 5, 8, 15, 23, 38]

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

result = select(int, data)
print(result)
result = where(lambda x: x % 2 == 0, result)
print(result)
result = select(lambda x: (x, x**2), result)
print(result)