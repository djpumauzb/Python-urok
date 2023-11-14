'''
Po dannomu celomu neotricatel'nomu 'n' vichislite znachenie n!.
N! = 1 * 2 * 3 * ... * N
0! = 1
Reshat zadachu ispolzuya while loop

Input: 5
Output: 120
'''
n = int(input("Vvedite chislo faktoriala: "))

if n < 0:
    print("Faktorial nebivaet v negativnix chislax :)")
elif n == 0:
    answer = 1
    print(f"{n} => {answer}")
elif n != 0:
    answer = 1
    i = n
    while i > 1:
        answer *= i
        i -= 1
    print(f"{n} => {answer}")