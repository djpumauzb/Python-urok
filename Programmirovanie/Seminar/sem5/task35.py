'''
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)

Input: 5
Output: yes 
'''


def prime(n: int):
    for i in range(2, n):
        if n % i == 0:
            return 'no'
    return 'yes'


print(prime(7))

# better way


def prime(n: int):
    for i in range(2, n // 3):
        if n % i == 0:
            return 'no'
    return 'yes'


print(prime(19))
