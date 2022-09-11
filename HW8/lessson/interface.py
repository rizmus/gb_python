from datetime import datetime

from taks_processing import create_job, delete_job, print_job, unlog_sys

x = 0

def login(names):
    ok = False
    print("Добрый день! Необходимо залогиниться")
    print(f"{names}")
    print("Представьтесь, кто Вы?")
    while not ok:
        x = input("Введите число от 1 до 4: ")
        if x.isdigit() and 1 <= int(x) <= 4:
            ok = True
        else:
            print("Вы ошиблись!")
    return x


def inp_date(date):
    d = input("Введите дату: ")


def inp_period(perod):
    ok = False
    print("Выберите период времени")
    print(f"{period}")
    while not ok:
        x = input("Введите число от 1 до 3: ")
        if x.isdigit() and 1 <= int(x) <= 3:
            ok = True
        else:
            print("Вы ошиблись!")
    return x


def inp_menu(menu):
    ok = False
    print("Что Вы хотите сделать?")
    print(f"{menu}")
    while not ok:
        x = input("Введите число от 1 до 4: ")
        if x.isdigit() and 1 <= int(x) <= 4:
            ok = True
        else:
            print("Вы ошиблись!")
    return x


def inp_txt():
    return input("Опишите суть дела: ")


names = ("1. Константин 2. Лада 3. Вадим 4. Сергей")
menu = ("1. Создать дело 2. Удалить дело 3. Вывести все дела 4. Разлогиниться")
period = ("1. Утро 2. День 3. Вечер")

name_kode = int(login(names))
while True:
    menu_kode = int(inp_menu(menu))

    if menu_kode == 1:
        date = input("Введите дату в формате ДД.ММ.ГГГГ: ")
        time_kode = int(inp_period(period))
        text_delo = inp_txt()
        Flag = create_job(name_kode, date, time_kode, text_delo)
        if Flag:
            print("Дело успешно создано")

    if menu_kode == 2:
        date = input("Введите дату в формате 01.01.2000")
        time_kode = int(inp_period(period))
        Flag1 = delete_job(name_kode, date, time_kode)
        if Flag1:
            print("Дело успешно удалено")

    if menu_kode == 3:
        date = input("Введите дату в формате 01.01.2000")
        print(print_job(name_kode, date))

    if menu_kode == 4:
        unlog_sys(name_kode)
        break

