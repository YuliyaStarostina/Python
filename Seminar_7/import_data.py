import datetime
import record

def input_format1(entry):

    with open('phone_directory.csv', 'a') as file:
        file.write(f'{entry[0]}\n{entry[1]}\n{entry[2]}\n{entry[3]}\n\n')

def input_format2(entry):

    with open('phone_directory.csv', 'a') as file:
        file.write(f'{entry[0]};{entry[1]};{entry[2]};{entry[3]}\n\n')
        