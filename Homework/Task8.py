# Задайте список из n чисел последовательности (1+\frac 1 n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6 ->14.07
n = int(input('Введите число: '))
def sequence(n):
    return [round((1 + 1 / x)**x, 2) for x in range(1, n + 1)]
print(sequence(n))
print(round(sum(sequence(n)), 2))# два знака поле запятой
