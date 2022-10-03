# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
with open('words.txt', 'w') as data:
    data.write('После каждого заката неабв наступает закатабв рассвет\n')


with open('words.txt', 'r') as line:
    old_data = line.read()


def delt_char(text):
    new_text = " ".join(filter(lambda x: 'абв' not in x, text.split()))
    return new_text


with open('words.txt', 'w') as new_line:
    new_data = delt_char(old_data)
    new_line.write(new_data)
print('Исходный текст: ')    
print(old_data)   
print('Итоговый текст: ') 
print(new_data)