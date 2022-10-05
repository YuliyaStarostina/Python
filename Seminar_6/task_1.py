# # Напишите программу вычисления арифм выражения, заданного строкой.

# print("Ноль в качестве операции завершит работу программы")
# while True:
#     s = input("Знак (+, -, *, /): ")
#     if s == "0":
#         break
#     if s not in ('+', '-', '*', '/'):
#         continue

#     x = float(input('x = '))
#     y = float(input('y = '))
#     if s == '+':
#         print('%.2f' % (x+y))
#     elif s == '-':
#         print('%.2f' % (x-y))
#     elif s == '*':
#         print(x * y)
#     elif s == '/':
#         if y != 0:
#             print(x/y)
#         else:
#             print('Делить на ноль нельзя!')
#     else:
#         print('Не верный знак операции')
line_ = '1-2*3+8/4'


def pol_to_list(line):
    itog = []
    for item in line:
        if item.isdigit():
            itog.append(int(item))
        else:
            itog.append(item)
    return itog


def count(lst):
    tmp = []
    index = 0
    print(lst)
    while index < len(lst):
    # while index < len(lst):
        if type(lst[index]) is int:
            tmp.append(lst[index])
        elif lst[index] == '+':
            tmp.append(lst[index + 1])
            index += 1
        elif lst[index] == '-':
            tmp.append(-lst[index + 1])
            index += 1
        elif lst[index] == '*':
            tmp[-1] = tmp[-1] * lst[index + 1]
            index += 1
        elif lst[index] == '/':
            tmp[-1] = tmp[-1] / lst[index + 1]
            index += 1
        index += 1
        print(tmp)

    return sum(tmp)


print(count(pol_to_list(line_)))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
a = [1, 2, 3, 5, 1, 5, 3, 10]

seen = set()
good = set()

for item in a:
    if item in seen:
        good.discard(item)
    else:
        seen.add(item)
        good.add(item)

print(good)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
line_ = '-1-222*3+48/4'


def pol_to_list(line):
    itog = []
    last_op = -1
    for index in range(len(line)):
        if index == 0 and line[index] == '-':
            last_op = index
            itog.append('-')
            continue
        if not line[index].isdigit():
            itog.append(int(line[last_op + 1:index]))
            itog.append(line[index])
            last_op = index
    itog.append(int(line[last_op + 1:]))
    return itog


def count(lst):
    tmp = []
    index = 0
    print(lst)
    flag = False
    for index in range(len(lst)):
        # while index < len(lst):
        if flag:
            flag = False
            continue
        if type(lst[index]) is int:
            tmp.append(lst[index])
        elif lst[index] == '+':
            tmp.append(lst[index + 1])
            flag = True
            # index += 1
        elif lst[index] == '-':
            tmp.append(-lst[index + 1])
            flag = True

            # index += 1
        elif lst[index] == '*':
            tmp[-1] = tmp[-1] * lst[index + 1]
            flag = True

            # index += 1
        elif lst[index] == '/':
            tmp[-1] = tmp[-1] / lst[index + 1]
            flag = True

            # index += 1
        # index += 1
        print(tmp)

    return sum(tmp)


print(count(pol_to_list(line_)))
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
line_ = '1-2*3+8/4'


def pol_to_list(line):
    itog = []
    for item in line:
        if item.isdigit():
            itog.append(int(item))
        else:
            itog.append(item)
    return itog


def count(lst):
    tmp = []
    index = 0
    print(lst)
    flag = False
    for index in range(len(lst)):
        # while index < len(lst):
        if flag:
            flag = False
            continue
        if type(lst[index]) is int:
            tmp.append(lst[index])
        elif lst[index] == '+':
            tmp.append(lst[index + 1])
            flag = True
            # index += 1
        elif lst[index] == '-':
            tmp.append(-lst[index + 1])
            flag = True

            # index += 1
        elif lst[index] == '*':
            tmp[-1] = tmp[-1] * lst[index + 1]
            flag = True

            # index += 1
        elif lst[index] == '/':
            tmp[-1] = tmp[-1] / lst[index + 1]
            flag = True

            # index += 1
        # index += 1
        print(tmp)

    return sum(tmp)


print(count(pol_to_list(line_)))










