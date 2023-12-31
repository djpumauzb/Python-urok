'''
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа. 
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не превосходящее 10^5.
Программа должна вывести  все пары дружественных чисел, каждое из которых
не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами.
Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

Inpt: 300
Outpt: 220 284
'''
def divisors(n: int):
    sum_divisors = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors


def main():
    k = int(input('введите верхнюю границу (но не более 100 000): '))
    if k <= 100_000:
        for i in range(1, k):
            x = divisors(i)
            if i < x <= k and i == divisors(x):
                print(i, x)
    else:
        print('Вы ввели слишком большое число.')

if __name__ == '__main__':
    main()
