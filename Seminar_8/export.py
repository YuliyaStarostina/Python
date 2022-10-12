def print_baza(last_name):
    with open('baza.txt', 'r', encoding='utf-8') as file:
        info_list = file.read().splitlines()
        for person in info_list:
            if last_name in person:
                print(person)
