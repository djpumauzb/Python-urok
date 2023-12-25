# colors = ['red', '99889', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

with open('file.txt', 'w') as data:
		data.write('line 1\n')
		data.write('line 2\n')