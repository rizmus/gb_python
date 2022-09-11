# from main import main_menu

# Проверка на наличие email
def user_mail_uniq(email):
    with open('users.txt', 'r') as file:
        for line in file:
            if email in line:
                return True


# Создать пользователя
def add_user():
    name = input('Введите имя: ')
    email = input('Введите email: ')
    if user_mail_uniq(email) is None:
        print('Ваше имя: ', name, '\nВаш email: ', email)
        answer = input('Данные введены  верно? (Да/Нет): ')
        if answer == 'Да':
            file = open(name+'.txt', 'w')
            file.close()
            user = name, email, (name+'.txt'), ('\n')
            with open('users.txt', 'a') as file:
                file.write(' | '.join(user))
        elif answer == 'Нет':
            add_user()
    else:
        print('Данный email уже занят, попробуйте еще раз')
        add_user()


#Выбрать пользователя
def current_user():
    email = input('Введите ваш email: ')
    with open('users.txt', 'r') as file:
        for line in file:
            if email in line:
                print('Успешный вход в ситему')
                return email
            else:
                print('Пользователь с таким email не найден')
                return False

