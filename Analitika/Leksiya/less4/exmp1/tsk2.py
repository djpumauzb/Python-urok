'''
S kalivaturi vvoditsya nekiy nabor chisel, b kachestve razdelitelya
ispolzuetsya probel. Etot nabor chisel budet schitan v kachestve stroki
Kak prevretit list str na list int?
'''
data = input('Vvedite danni dlya spiski: ')
data = list(map(int, data.split()))

print(data)