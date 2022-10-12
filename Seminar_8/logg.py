from itertools import count


def log_info(info):
    with open('log.txt', 'a', encoding='UTF-8') as f:
        if len(info.split()) == 1:
            f.write(f'поиск - {info}' + '\n')
        else:
            f.write(f'ввод - {info}' + '\n')


