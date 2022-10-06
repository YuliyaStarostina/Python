
def read_all_file():
    with open('telefonsbook.csv', 'r') as file:
        for line in file:
            print(line)