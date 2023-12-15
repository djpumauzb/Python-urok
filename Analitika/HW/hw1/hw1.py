"""
Найдите сумму цифр трехзначного числа n.
Результат сохраните в перменную res.

Пример:
n = 123 -> res = 6 (1 + 2 + 3)
n = 100 -> res = 1 (1 + 0 + 0)

"""

n = 123

## 1st method ##
# str_n = str(n)
# res = int(str_n[0]) + int(str_n[1]) + int(str_n[2])
# print(f"n = {n} -> res = {res} ({str_n[0]} + {str_n[1]} + {str_n[2]})")

res = n % 10 + (n // 10) % 10 + n // 100
print(res)