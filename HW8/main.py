from login import add_user, current_user
from initiation import file_initiation, user_initiation

print('Программа учета дел')
sub_menu_val = ("1. Создать дело 2. Удалить дело 3. Вывести все дела 4. Разлогиниться")

def main_menu():
    print('1. Авторизация\n2. Регистрация\n3. Выход')
    selection_number = input('Выберете пункт: ')
    if int(selection_number) == 1:
        sub_menu(current_user())
    elif int(selection_number) == 2:
        add_user()
    elif int(selection_number) == 3:
        print('Работа завершена')
    else:
        print('Не верный выбор, попробуйте еще раз')


def sub_menu(email):
    data = file_initiation(user_initiation(email))
    print(sub_menu_val)
    selection_number = int(input('Выберете пункт: '))
    if selection_number == 3:
        for key, value in data.items():
            print(key, value)


main_menu()

