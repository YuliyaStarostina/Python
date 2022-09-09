'''Задание 5 Реализуйте алгоритм перемешивания списка.'''
import random


lst = list(range(2, 100, 10))
print(lst)
def mix_list(lst):
    new_lst = lst.copy()
    for i in range(len(new_lst)):
        ind_rand = random.randint(0, len(new_lst) - 1)
        temp = new_lst[i]
        new_lst[i] = new_lst[ind_rand]
        new_lst[ind_rand] = temp
    return new_lst
print(mix_list(lst))
    
 