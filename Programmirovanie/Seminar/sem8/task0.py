# file = open('name.txt', 'w', encoding='utf-8')
# print(file)
# print(type(file))
# file.close()

# with

with open('name.txt', 'r', encoding='utf-8') as fd:
    fd.write('Example text\n')

with open('name.txt', 'r', encoding='utf-8') as fd:
    fd.readlines()