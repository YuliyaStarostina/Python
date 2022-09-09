# Задание 6 Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Пример
#-Для "abababb" и "aba" -> 2'''
stroka_1 = "treetreetree"
stroka_2 = "ree"
count = 0
i = 0
while i < len(stroka_1):
    if stroka_1[i:i + len(stroka_2)] == stroka_2:
        count += 1
        i += 1
    else:
        i += 1
print(f'Вторая строка входит в первую строку {count} раза')
