'''
 Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
 Поскольку разобраться в его кричалках не настолько просто, 
 насколько легко он их придумывает, Вам стоит написать программу. 
 Винни-Пух считает, что ритм есть, если число слогов (т.е. число 
 гласных букв) в каждой фразе стихотворения одинаковое. Фраза 
 может состоять из одного слова, если во фразе несколько слов, 
 то они разделяются дефисами. Фразы отделяются друг от друга 
 пробелами. Стихотворение  Винни-Пух вбивает в программу с 
 клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом 
 все в порядке и “Пам парам”, если с ритмом все не в порядке

 Input:
 пара-ра-рам рам-пам-папам па-ра-па-дам

 Output:
 Парам пам-пам
'''


def check_rhythm(say, volwes):
    phrases = say.split()
    if len(phrases) <= 1:
        return "Количество фраз должно быть больше одной!"

    syllable_counts = [sum(1 for char in phrase if char.lower() in volwes) for phrase in phrases]
    # if say == 'по-русски говорят':
    #     return 'Парам пам-пам'
    if all(count == syllable_counts[0] for count in syllable_counts):
        return "Парам пам-пам"
    else:
        return "Пам парам"

volwes = 'аяюоеёэиы'
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
result = check_rhythm(stroka, volwes)
print(result)

# Norm reshenie:

vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
phrases = stroka.split()

if len(phrases) < 2:
    print('Количество фраз должно быть больше одной!')
else:
    count_vowels = [sum(1 for char in phrase if char.lower() in vowels) for phrase in phrases]

    if count_vowels.count(count_vowels[0]) == len(count_vowels):
        print('Парам пам-пам')
    else:
        print('Пам парам')
