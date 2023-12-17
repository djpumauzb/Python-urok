'''
Polzovatel vvodit teskt(stroka). Slovom schitaetsya
posledovatelnost' neprobelnix simvolov idushix
podryad, slova rezdeleni odnim ili bolshim chislom probelov.
Opredelite skolko razlichnix slov soderjitsya v etom tekste.

Inpt: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells

Oupt: 13
'''
text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".split()
set_1 = set()

for i in text:
    set_1.add(i.lower())
print(len(set_1))

