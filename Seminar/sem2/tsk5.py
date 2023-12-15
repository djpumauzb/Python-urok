'''
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1

Input: 5
Output: 6
'''
# 0 1 2 3 4 5 6  7  8
# 0 1 1 2 3 5 8 13 21...
num = int(input("Veedite chislo: "))

fib_list = [0, 1]
while fib_list[-1] < num:
    fib_list.append(fib_list[-2] + fib_list[-1])
    #print(fib_list)

#print(fib_list[-1])
if fib_list[-1] == num:
    print(len(fib_list))
else:
    print(-1)

#### Other way non massiv : ###

count = 3   # 0 1 1 - bo'ganiga
prev = 1
fib = 1
while fib < num:
    prev, fib = fib, fib + prev
    count += 1
if num < 2:
    print("Vvedite chislo bolshe 1")
elif fib == num:
    print(count)
else:
    print(-1)



# New tactics
# a = 3
# b = 4
# t = a
# a = b
# b = t
# print(a, b)
### or ###
# a, b = b, a
# print (a, b)
# 4, 3
# 4, 3

