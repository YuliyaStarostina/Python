# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.'''

n = int(input ('Введите число ' ))
spisok = list(range(-n, n + 1))
print(spisok)
a = int(input('Введите номер позиции первого числа '))
b = int(input('Введите позицию второго числа  '))
print(f'Произведение элементов на позициях a и b = {spisok[a-1] * spisok[b-1]} ')