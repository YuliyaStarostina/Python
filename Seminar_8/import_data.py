def add(some_person):
    with open("baza.txt", "a", encoding= "utf-8") as my_file:
        my_file.write(f'{some_person}' +'\n')
    