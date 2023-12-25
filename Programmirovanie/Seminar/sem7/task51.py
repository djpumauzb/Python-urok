'''
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение 
некоторой характеристики, и возвращают True, если это так. 
Если значение характеристики для разных объектов 
отличается - то False. Для пустого набора объектов, 
функция должна возвращать True. Аргумент characteristic - это 
функция, которая принимает объект и вычисляет его характеристику.
'''
# Inpit:
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

# Output:
# same


def same_by(characteristic, objects):
    if len(objects) == 0:
        return True
    pattern = characteristic(objects[0])
    res = list(filter(lambda x: characteristic(x) == pattern, objects))
    return all(res)

values = [0, 2, 10, 6]

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
