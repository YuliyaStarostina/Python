# Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def predicat_true(x, y, z):
    print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}')


predicat_true(0, 0, 0)
predicat_true(0, 0, 1)
predicat_true(0, 1, 0)
predicat_true(0, 1, 1)
predicat_true(1, 0, 0)
predicat_true(1, 0, 1)
predicat_true(1, 1, 0)
predicat_true(1, 1, 1)
