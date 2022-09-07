# типы даных и переменная
# int, float, boolean, str, list, None
# для того, чтобы воспользоваться переменной, можно сначала присвоить ей значение None
from re import S


valeu = None
a = 123
b = 1.23
# для того, чтобы узнать тип данных, перед переменной добавляют функцию type
# print(type(a))
# print(type(b))
valeu = 12345
print(valeu)
# для строковых данных указываем:
s = 'Hello world'
print(s)  # вывод строки
# второй вариант использования кавычек
s = "hello 'worid"  # s = 'hello \ 'world', s = 'hello \n 'world' - перенос на другую строку
# для вывода на печать в одну строку делаем print(a, b, valeu)
print(a, '-', b, '-', s)
# если необходимо вывести на экран значения в другом порядке, то необходио в фигурнах скобках просто поставить индексы этих значений
print('{} - {} - {}'.format(a, b, s))
print(f'{a} - {b} - {s}')
# логически перемнные
f = True
print(True)

# применение списков
list = []
print(list)
# Ввод и вывод данных пользователя
print('Введите а')
a = int(input())
print('Введите b')
b = int(input())
print(a, '+', b, '=', a + b)
# арифметические операции
# +, -, *, /, %, //, **
# Приоритет операций
# **, ⊕, ⊖, *, /, //, %, +, -( ) Скобки меняют приоритет
exp1 = 2**3 - 10 % 5 + 2*3
exp2 = 2**3 - 10 / 5 + 2*3
print(exp1)  # 14.0 или 14
print(exp2)  # 12.0 или 12
exp1 = 2**3 - 10 % 5 + 2*3
exp2 = (2**3) - (10 / 5) + (2*3)
print(exp1)  # 14.0 или 14
print(exp2)  # 12.0 или 12
# Сокращённые операции и операции присваивания
# Демонстрация
iter = 2
iter += 3  # iter = iter + 3
iter -= 4  # iter = iter - 4
iter *= 5  # iter = iter * 5
iter /= 5  # iter = iter / 5
iter //= 5  # iter = iter // 5
iter %= 5  # iter = iter % 5
iter **= 5  # iter = iter **
a, b, c = 1, 2, 3
# a: 1 b: 2 c: 3
print('a: {} b: {} c: {}'.format(a, b, c))
range(*(1, 5, 2))  # указываем сколько знаков после запятой нужно прописать
# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

# Управляющие конструкции: if, if-else
# Условный оператор позволяет управлять ходом выполнения программы
username = input('Введите имя: ')
if (username == 'Маша'):
    print('Ура, это же МАША!')
else:
    print('Привет, ', username)

    # Управляющие конструкции: if, if-else
username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)

    # Управляющие конструкции: while
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
print(inverted)  # перевернутое число (из 23 получили 32)

# управляющие конструкции: while-else
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит )')
print(inverted)
# Пожалуй
# хватит )
# 32
# Управляющие конструкции for
for i in 1, -2, 3, 14, 5:
    print(i**2)

# Знакомьтесь – range
r = range(5)  # range(0, 5)
r = range(2, 5)  # range(2, 5)
r = range(-5, 0)  # range(-5, 0)
r = range(1, 10, 2)  # range(1, 10, 2)
r = range(100, 0, -20)  # range(100, 0, -20)
r = range(5)  # range(0, 5)
r = range(2, 5)  # range(2, 5)
r = range(-5, 0)  # range(-5, 0)
r = range(1, 10, 2)  # range(1, 10, 2)
r = range(100, 0, -20)  # range(100, 0, -20)
r = range(100, 0, -20)  # range(100, 0, -20)
for i in r:
    print(i)
# 100 80 60 40 20
for i in range(5):
    print(i)
# 0 1 2 3 4

# вложенные циклы
line = ""
for i in range(5):
    line = ''
    for j in range(5):
        line += ['*']
    print(line)
# немного о строках

text = 'съешь ещё этих мягких французских булок'
print(len(text))  # 39
print('ещё' in text)  # True
print(text.isdigit())  # False
print(text.islower())  # True
print(text.replace('ещё', 'ЕЩЁ'))
for c in text:
    print(c)
    text = 'съешь ещё этих мягких французских булок'
print(text[0])  # c
print(text[1])  # ъ
print(text[len(text)-1])  # к
print(text[-5])  # б
print(text[:])  # print(text)
print(text[:2])  # съ
print(text[len(text)-2:])  # ок
print(text[2:9])  # ешь ещё
print(text[6:-18])  # ещё этих мягких
print(text[0:len(text):6])  # сеикакл
print(text[::6])  # сеикакл
text = text[2:9] + text[-5] + text[:2]  # ...

# Список – пронумерованная, изменяемая коллекция объектов произвольных типов
#Списки: введение
numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers)  # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers)  # [10, 2, 3, 4, 5]
for i in numbers:
    i *= 2
    print(i)  # [20, 4, 6, 8, 10]
print(numbers)  # [10, 2, 3, 4, 5]

colors = ['red', 'green', 'blue']
for e in colors:
    print(e)  # red green blue
for e in colors:
    print(e*2)  # redred greengreen blueblue
colors.append('gray')  # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray'])  # True
colors.remove('red')  # del colors[0] # удалить элемент


# Функции обозначаются def, далее название и значение


def f(x):
    if x == 1:
      return 'Целое'
    elif x == 2.3:
      return 23
    else:
     return
arg = 1
print(f(arg))  # Целое
print(type(f(arg)))


print(f(2.3))  # 23
print(f(28))  # None
print(type(f(1)))  # str
print(type(f(2.3)))  # int
print(type(f(28)))  # NoneTyp
