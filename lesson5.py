from random import randint
from time import sleep

def input_player():
    while True:
        user_move = input('Сколько конфет вы берете?\n')
        if user_move.isdigit() and int(user_move) < 29:
            user_move = int(user_move)
            return user_move
        else:
            print('Количество введено не корректно!\nНеобходимо ввести количество от 1 до 28.')


def rand_bot(result):
    value = result
    while result - value <= 29:
        value = randint(1, 28)
    return value


count_game = 2021
players_list = ['user', 'bot']
count_player = 0

print('Добро пожаловать в консольную игру!\nУ вас с ботом есть 2021 конфета!\nВы можете взять от 1 до 28 конфет\nПобедит тот, кто заберет конфеты последним!\nДа начнется битва! :)')
sleep(2)
print('')

dim = input('2021 - долгая игра, можем сократить до 250 конфет.\nСогласны - набрать Да, не согласны - любой символ: ')

if dim == 'Да':
    count_game = 250
    print('Теперь конфет 250')
else:
    print('Конфет осталось 2021')


while count_game != 0:

    print('\nХод пользователя:', players_list[count_player])

    if count_player == 0:
        user_move = input_player()
        count_player = 1
    else:
        if count_game > 57:
            user_move = rand_bot(count_game)
        else:
            user_move = randint(1, 28)
        print('Компьютер забрал:', user_move, 'конфет')
        count_player = 0

    count_game -= user_move
    sleep(1)
    print('Остаток конфет:', count_game)
    sleep(1)
    if count_game < 29:
        print('Победил игрок: ', players_list[count_player])
        break
