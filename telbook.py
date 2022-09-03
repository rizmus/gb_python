import functools

first_name_list = []
surname_list = []
tel_list = []
description_list = []


#Импорт в телефонную книгу
def import_data_book(file, separator):
    f = open(file, 'r')
    count = 0
    tmp_list = []
    for i in f:
        tmp_list = i.split(separator)
        first_name_list.append(tmp_list[0])
        surname_list.append(tmp_list[1])
        tel_list.append(tmp_list[2])
        description_list.append((tmp_list[3]))
        tmp_list.clear()
        count += 1
    print('Добавлено', count, 'записей.')


def export_data_book(file):
    f = open(file, 'w')
    tmp_list = []
    for index, item in enumerate(first_name_list):
        tmp_list.append(first_name_list[index])
        tmp_list.append(surname_list[index])
        tmp_list.append(tel_list[index])
        tmp_list.append(description_list[index])
        temp_line = ';'.join(tmp_list)
        f.write(temp_line + '\n')
        tmp_list.clear()
    f.close()
export_data_book('test.txt')

# Ввод данных:
def add_contact():
    print('\nДобавление нового контакта')
    first_name_list.append(input('Введите имя: '))
    surname_list.append(input('Введите фамилию: '))
    tel_list.append(input('Введите телефон: '))
    description_list.append(input('Введите описание: '))
    print('Контакт успешно записан')


# Проверка на пустоту перед выводом:
def check_for_emptiness(list, index):
    if list[index] != '':
        print(list[index])


# Вывод одного контакта:
def view_one_item(index):
    print('---')
    print('ID:', index+1)
    check_for_emptiness(first_name_list, index)
    check_for_emptiness(surname_list, index)
    check_for_emptiness(tel_list, index)
    check_for_emptiness(description_list, index)

#Удаление контакта
def remove_one_item(id):
    id = int(id)
    first_name_list.remove(id)
    surname_list.remove(id)
    tel_list.remove(id)
    description_list.remove(id)
    print('Контакт с ID', id, 'удален.')


# Ввод всех данных:
def view_book():
    print('В записаной книге:', len(first_name_list), 'записей.')
    for index, item in enumerate(first_name_list):
        view_one_item(index)

# Поиск
def find_book(item):
    count = 0
    for index, val in enumerate(first_name_list):
        if val == item:
            view_one_item(index)
            count += 1
    for index, val in enumerate(surname_list):
        if val == item:
            view_one_item(index)
            count += 1
    for index, val in enumerate(tel_list):
        if val == item:
            view_one_item(index)
            count += 1
    for index, val in enumerate(description_list):
        if val == item:
            view_one_item(index)
            count += 1
    if count == 0:
        print('Нет совпадений.')


def menu_book():
    print('\n---')
    print('\nМеню программы')
    print('Добавить новый контакт: add')
    print('Удалить контакт: remove')
    print('Посмотреть контакты: list')
    print('Импортировать из txt файла: import')
    print('Экспортировать в файл: export')
    print('Поиск по книге: find')
    print('Выйти из программы: exit')
    menu_item = input('Введите команду: ')
    if menu_item == 'add':
        add_contact()
        print('')
        menu_book()
    elif menu_item == 'list':
        view_book()
        menu_book()
    elif menu_item == 'remove':
        view_book()
        remove_one_item(input('Введите ID для удаления контакта: '))
        menu_book()
    elif menu_item == 'import':
        import_data_book(input('Введите название файла: '), input('Введите разделитель: '))
        menu_book()
    elif menu_item == 'export':
        import_data_book(input('Введите название файла: '))
        menu_book()
    elif menu_item == 'find':
        find_book(input('Введите данные для поиска: '))
        menu_book()
    elif menu_item == 'exit':
        print('До скорых встреч!')
        return
    else:
        print('Произошла ошибка, попробуем еще?')
        menu_book()


menu_book()
