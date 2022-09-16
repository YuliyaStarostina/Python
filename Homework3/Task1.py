# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

spisok = [2, 3, 5, 9, 3]
def sum_odd(ls):
    sum = 0
    for n in range(len(spisok)):
        if n % 2 != 0 and n != 0:
            sum += spisok[n]
    else:
        n += 1
    return sum
print(sum_odd(spisok))


# ////////////////////////////////////////////////////////////////////////////////////////
# spis = [int(i) for i in input('Введите числа через пробел: ').split()]
#
# def summ_odd(lst):
#     lst = spis[1::2]
#     print(lst)
#     print(sum(lst))
#     return
#
# summ_odd(spis)

'''2.Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''

# spsk = [2, 3, 4, 5, 6]
#
# def pair_number(lst):
#     sqrt = []
#     for i in range((len(lst) + 1) // 2):
#         sqrt.append(lst[i] * lst[len(lst)-1-i])
#     return sqrt
#
# print(pair_number(spsk))


'''3.Задайте список из вещественных чисел. Напишите программу, 
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

# my_list = [float(i) for i in input('Введите вещественные числа через пробел: ').split()]
# # # print(my_list)
# # def max_min_fractional(lst):
# #     new_list = []
# #     for i in my_list:
# #         if i % 1 != 0:
# #             new_list.append(round(i % 1, 2))
# #     rez = max(new_list) - min(new_list)
# #     print(f'Разница между макс и мин значением дробной части элементов = {rez}')
# #     return
# #
# # max_min_fractional(my_list)
# # ////////////////////////////////////////////////////////////////////////////////////////////
# new_list = [round(i % 1, 2) for i in my_list if i % 1 != 0]
# print(f'Разница между макс и мин значением дробной части элементов = {max(new_list) - min(new_list)}')

'''4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10'''

# number = int(input('Please input integer: '))

# def transform_binary(num):
#     res = ''
#     while num > 0:
#         res = str(num % 2) + res
#         num = num // 2
#     return res
#
# print(f'Binary: {transform_binary(number)}')

# print(bin(int(input('Please input integer: '))))

'''5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]'''

# number = int(input('Please, input number: '))
#
# def fibonacci(num):
#     fibo = []
#     n1, n2 = 1, 1
#     for i in range(num):
#         fibo.append(n1)
#         n1, n2 = n2, n1 + n2
#     n1, n2 = 0, 1
#     for i in range(num+1):
#         fibo.insert(0, n1)
#         n1, n2 = n2, n1 - n2
#     return fibo
#
# print(fibonacci(number))
