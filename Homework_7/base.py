# with open('data_base.csv', 'w+') as data:
#     data.write('Петров Иван Иванович 89174562456 коллега\n')
#     data.write('Кукушкин Авдон Авдеевич 89189522335 юрист\n')
#     data.write('Любимцев Исхак Исхакович 89873214598 историк\n')
# Функция encode() и decode() - кодирование строк, возвращает объект байтов, по умолчанию используется utf-8
# mode -  строка, которая указывает режим, в котором открывается файл. По умолчанию 'r'.


import csv
with open("telefonsbook.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(["Фамилия", "Имя", "Отчество", "Телефон", "Описание"])
    file_writer.writerow(["Синицын", "Евгений", "Иванович", "89864531234", "коллега"])
    file_writer.writerow(["Панкова", "Ольга", "Антоновна", "89187863412", "репетитор"])
    file_writer.writerow(["Серохвостова", "Оксана", "Вячеславовна", "83814568760", "доктор"])