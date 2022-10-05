def record():
    entry = []
    surname = input('Введите фамилию: ')
    entry.append(surname)
    name = input('Введите имя: ')
    entry.append(name)
    phone = input('Введите телефон: ')
    entry.append(phone)
    description = input('Введите описание контакта: ')
    entry.append(description)
    print('Вами введена запись: ', entry)
    return entry
