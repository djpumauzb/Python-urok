'''
Napishite programmu dlya pechati vsex unikalnix znacheniy v slovare.

Input: list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

Output: {'S005', 'S009', 'S001', 'S002', 'S007'}

'''

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

set_1 = set()

for i in list_1:
	for j in i:
		set_1.add(i[j])
print(set_1)