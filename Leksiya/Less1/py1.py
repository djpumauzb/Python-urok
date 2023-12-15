# Vvod dannix
# print("Vvedite pervuyu stroku: ")
# a = input()
# print(a)

# next ver
# print("Vvedite 1oe chislo: ")
# b = input()
# b1 = input("Vvedite 2oe chislo: ")
# print(f"{b} + {b1} = {b + b1}")
# # result 5 + 7 = 57 xD

# c = 5.89
# print(c)
# print(type(c))
# c = int(c)
# print(c)
# print(type(c))
# c = str(c)
# print(c)
# print(type(c))
# c = 1
# c = bool(c)
# print(c)
# print(type(c))
# # 5.89
# # <class 'float'>
# # 5
# # <class 'int'>
# # 5
# # <class 'str'>
# # 1
# # <class 'bool'>

# next ver2
print("Vvedite 1oe chislo: ")
b = int(input())
b1 = int(input("Vvedite 2oe chislo: "))
print(f"{b} + {b1} = {b + b1}")
# 5 + 6 = 11

# operatsii
a = 5.986489
b = 6.561561
print(a*b)
# 38.xxxxxxxxxxxx
# s funksiey round() mojno ogranichit znachenie posle zayyatoi
# round(result, skolko zncahenie posle ,) | round(a*b, 3)
print(round(a*b, 3))

# shetchiki
i = 1
i += i
i += 3 # i = i + 3
i //=5 # i = i ** 5

# logicheskie operacii
a = 1 < 4 and 5 > 2
a = 1 < 4 & 5 > 2
a = 1 < 3 < 5 < 10


# Uslovie IF ELSE
# if contd:
#     oper
# elif cond:
#     oper
# elif cond:
#     oper
# else cond:
#     oper

# slojnie uslovie
# and | or | not
# if cond and cond2:
#   oper
# else cond3 or cond4:
#   oper


 # loops
 # while cond:
    # oper1
    # oper2
        #....
        # oper n

# While-esle Upravlayushie konstrukcii:
# while cond:
    # oper 1
    # oper 2
# else:
    # oper n+1
    # oper n+2

## Else vishe bduet rabotat kogda while budet zavershatsya SAMOSTOYATELNO!
## esli budet break ELSE ne budet rabotat:

i = 0
while i < 5:
    if i==3:
        break
    i += 1
else:
    print("else rabotaet")
print(i)

# OOP nebudet ispolzovat "break" i ne stoit voobshe ispolzovat break )
# dlya etogo est metog flaga "flag":

n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0:
        flag = False # esli ostatok prio deleni chisla n na i raven 0
        print(i)
    elif i > n // 2: # delit' chisla ne mojet perevishat' vvedennoe chislo, delennoe na 2
        print(n)
        flag = False
    i += 1
# [vvedem] 25
# [otvet] 5


# Sikl for, funksiya range():
# for in enumeration:
    # oper 1
    # oper 2

# for i in 1, -2, 3, 4:
    # print(i)

# RANGE()
# range vidaet znachenie iz diapazona s shagom 1
# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(0, -5) # - - - -
# r = range(1, 10, 2) # 1 3 5 7
# r = range(100, 0, -20) # 100 80 60 40 20 

r = range(100, 0, -20)
for i in r:
    print(i)
# 100 80 60 40 20

for i in "qwerty":
    print(i)
# q
# w
# e
# r
# t
# y

####
line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "+"
    print(line)
# +++++
# +++++
# +++++
# +++++
# +++++


# len
text = "Syesh eshe etix myagkix fransuzkix bulok"
print("eshe" in text) # True or False
print(text.lower()) # Vse malenkimi bukvami
print(text.upper()) # Vse bolshimi bukvami
print(text.replace("eshe", "ESHE")) # zamenit
print(text[0]) # S
print(text[len(text)-1]) # k
print(text[:]) # Syesh eshe etix myagkix fransuzkix bulok
print(text[len(text)-2:]) # ok
print(text[2:9]) # esh eshe
print(text[0:len(text):6]) # seikakl
print(text[::6]) # seikakl
text = text[2:9] + text[-5] + text[:2] # ...
