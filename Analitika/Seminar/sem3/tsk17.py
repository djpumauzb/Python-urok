'''
Dan spsisok chisel.Opredelite, skolko v nem
vstrechaetsya razlichnix chisel

Input: [1,1,2,0,-1,3,4,4]
Output: 6
'''

list1 = [1, 1, 2, 0, -1, 3, 4, 4]

# noviy metod - funksiya set()

print(len(set(list1)))