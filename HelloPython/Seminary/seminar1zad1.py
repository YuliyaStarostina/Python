# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# Пример:
## 5, 25 - да
# 4, 16 - да
print('Введите первое число')
a = int(input())
print('Введите второе число')
b = int(input())
if b == a*a or a == b*b:
    print('yes')
else:
    print('no')
    