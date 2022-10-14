my_list = [1, 2, 3, 5, 8, 15, 23, 38]
new_list = list((x, x**2), filter(lambda x: (x%2 == 0), my_list))
print(new_list)