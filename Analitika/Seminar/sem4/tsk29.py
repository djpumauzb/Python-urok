'''
Vanya i Petya posprorili, kto bistree reshit
sledushuyu zadachu: "Zadana posledovatelnost' 
neotricatelnix celix chisel. Trebuyetsya opredelit'
zncahenie naibolshego elementa posledovatel'nosti, kotoraya
zavershaetsya pervim vstretibshimsya nulem (chislo 0 ne vxodit v posledovatel'nost')"
Odnako 2 druga okazalis ne takimi smishlennimi. Nikto iz rebyat ne smog do
konca sdelat' eto zdanie. Oni reshili tak: u kogo budet men'she oshibok v kode, tot i 
vigral spor. Za pomoshyu tovarishi obratilis k Vam, studentam.
'''
# Vanya:
n = int(input())
max_number = 1000 # oshibka 
while n != 0:
    n = int(input())
    if max_number > n: # oshibka
        max_number = n
print(max_number)

#Petya

n = int(input())
max_number = -1
while n < 0: # oshibka
    n = int(input())
    if max_number < n:
        n = max_number # oshibka
print(n) #oshibka


# Vanya wins :)