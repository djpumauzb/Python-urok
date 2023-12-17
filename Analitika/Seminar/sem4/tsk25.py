'''
Npaishite programmu, kotoraya prinimaet na vxod stroku, i otslejivaet,
skolko raz kajdiy simvol uje vstrechalsya. Kolichestvo povtorov dobavlaetsya 
k simvolam s pomoshyu postfiksa formata `_n`

Inpt: a a a b c a a d c d d
Oupt: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
'''
# Topshiriqni yechish uchun .split() funksiya-metodidan foydalaning

stroka = input().split()
res = {}

for i in stroka:
    if i in res:
        print(f'{i}_{res[i]}', end=' ') # agar end qo'yilmasa yangi qatordan chiqaradi.
    else:
        print(i, end=' ')        
    res[i] = res.get(i, 0) + 1 