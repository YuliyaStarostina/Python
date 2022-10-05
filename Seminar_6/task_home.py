'''Задача: предложить улучшения кода для уже решённых задач:
С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension'''

'''Задание 2 Напишите программу, которая принимает на 
вход число N и выдает набор произведений чисел от 1 до N.
Пример:
пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''
# Вариант №1
# from math import factorial
# n = int(input('Введите число: '))

# def mult(n):
#     i, j = 1, 2
#     lst = [1]
#     while i < n:
#         lst.append(j * lst[i - 1])
#         j += 1
#         i += 1
#     return lst
# print(mult(n))

# Вариант №2

# import math

# factorl = int(input('Введите число: '))
# print([math.factorial(i) for i in range(1, factorl +1)])


'''Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
округлённую до трёх знаков после точки.
Пример:
Для n = 6 -> 14.072'''
# Вариант №1

# num = int(input('Введите число: '))
#
# def spisok_posl(n):
#     tls = []
#     for i in range(1, n+1):
#         tls.append(round((1 + 1 / i) ** i, 3))
#     return tls
#
#
# def smm(ls):
#     sm=0
#     for i in range(len(ls)):
#         sm += ls[i]
#     return sm
#
# res = spisok_posl(num)
# print(f'{res}  Сумма = {smm(res)}')

# Вариант №2

# n = int(input('Введите число: '))
# print(round(sum([round((1 + 1 / x)**x, 3) for x in range(1, n + 1)]), 3))

'''3.Задайте список из вещественных чисел. Напишите программу, 
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''
# Вариант №1


#  my_list = [float(i) for i in input('Введите вещественные числа через пробел: ').split()]
# # print(my_list)
# def max_min_fractional(lst):
#     new_list = []
#     for i in my_list:
#         if i % 1 != 0:
#             new_list.append(round(i % 1, 2))
#     rez = max(new_list) - min(new_list)
#     print(f'Разница между макс и мин значением дробной части элементов = {rez}')
#     return

# max_min_fractional(my_list)
# # Варианте №2
# my_list = [float(i) for i in input('Введите вещественные числа через пробел: ').split()]
# new_list = [round(i % 1, 2) for i in my_list if i % 1 != 0]
# print(f'Разница между макс и мин значением дробной части элементов = {max(new_list) - min(new_list)}')


'''1. Задайте список из нескольких чисел. Напишите программу, 
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''
# Вариант №1


# spisok = [2, 3, 5, 9, 3]
#
# def sum_odd(ls):
#     sum = 0
#     for k in range(len(spisok)):
#         if k % 2 != 0 and k != 0:
#             sum += spisok[k]
#         else:
#             k += 1
#     return sum
#
# print(sum_odd(spisok))
# Вариант №2

# spis = [int(i) for i in input('Введите числа через пробел: ').split()]
#
# def summ_odd(lst):
#     lst = spis[1::2]
#     print(lst)
#     print(sum(lst))
#     return
#
# summ_odd(spis)
# Вариант №3
# from functools import reduce
# spis = list(map(int, input('Введите числа через пробел: ').split()))
# lst = spis[1::2]
# print(reduce(lambda x, y: x + y, lst))

