# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# spisok = [2, 3, 5, 9, 3]
# def sum_odd(ls):
#     sum = 0
#     for n in range(len(spisok)):
#         if n % 2 != 0 and n != 0:
#             sum += spisok[n]
#     else:
#         n += 1
#     return sum
# print(sum_odd(spisok))


# 2.Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:- [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]


# my_list = [int(i) for i in input('Введите числа через пробел: ').split()]

# def pair_number(lst):
#     sqrt = []
#     for i in range((len(lst) + 1) // 2):
#         sqrt.append(lst[i] * lst[len(lst)-1-i])
#     return sqrt

# print(pair_number(my_list))


# 3.Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# my_list = [float(i) for i in input('Введите вещественные числа через пробел: ').split()]

# print(my_list)
# def max_min_fractional_part(lst):
#     new_list = []
#     for i in my_list:
#         if i % 1 != 0:
#             new_list.append(round(i % 1, 2))
#     result = max(new_list) - min(new_list)
#     print(f'Разница между max и min значением дробной части элементов = {result}')
#     return

# max_min_fractional_part(my_list)


# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10'''

# from concurrent.futures.process import _ResultItem
# number = int(input('Задайте десятичное число: '))
# def binary_number(num):
#     result = ''
#     while num > 0:
#         result = str(num % 2) + result
#         num = num // 2
#     return result

# print(f'Число в двоичной системе: {binary_number(number)}')




# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input('Задайте число: '))

def fibonacci(num):
    fbnc = []
    n1, n2 = 1, 1
    for i in range(num):
        fbnc.append(n1)
        n1, n2 = n2, n1 + n2
    n1, n2 = 0, 1
    for i in range(num + 1):
        fbnc.insert(0, n1)
        n1, n2 = n2, n1 - n2
    return fbnc

print(f'Список чисел Фибоначчи: {fibonacci(number)}')
