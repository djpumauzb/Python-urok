'''
Последовательностью Фибоначчи называется
последовательность чисел a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

Требуется найти N-е число Фибоначчи

Input: 7
Output: 21
'''


def fibo(x, fib_list=[0, 1]):
    print('fibo list', fib_list)
    if len(fib_list) == x + 2:
        return fib_list[-1]
    fib_list.append(fib_list[-1] + fib_list[-2])
    return fibo(x, fib_list)


print(fibo(7))

# Better way


def fubo(x, m=0, n=1):
    if x == 0:
        return n
    # t = n
    # n = m + n
    # m = t
    m, n = n, m+n
    x -= 1
    return fubo(x, m, n)


print(fubo(7))

# Betterer way


def fubo(x, m=0, n=1):
    if x == 0:
        return n
    return fubo(x-1, n, m + n)


print(fubo(7))