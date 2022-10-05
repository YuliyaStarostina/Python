
def read_all_file():
    with open('phone_directory.csv', 'r') as file:
        for line in file:
            print(line)