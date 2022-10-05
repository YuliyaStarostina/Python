import record
import user_interface
import export_data
import import_data


def run():
    operation = user_interface.choise_operatoin()

    if operation == 1:
        print('Выбрана операция внесения нового контакта.')
        format = user_interface.choise_format()
        if format == 1:
            print('Формат: строка - разделитель.')

            import_data.input_format1(record.record())

        if format == 2:
            print('Формат: ";" - разделитель.')

            import_data.input_format2(record.record())

    if operation == 2:
        print('Выбрана операция вывода справочника.')

        export_data.read_all_file()
