
# 1 . Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Создайте абвпрограмму для игры с конфабветами человек против человека

f = open('text.txt', 'w')

text_value = input('Введите текст где необходимо убрать авб:\n')
text_abv = ' '.join(filter(lambda x: 'абв' not in x, text_value.split()))

f.write(text_abv)
f.close()

# 2. Создайте программу для игры с конфетами человек против человека.
#    Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#    a) Добавьте игру против бота
#    b) Подумайте как наделить бота ""интеллектом""



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
    if result <= 56 and result > 29:
        value = result - 29
    else:
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
        print('Компьютер забрал:', rand_bot(count_game), 'конфет')
        count_player = 0
        # if count_game > 29:
        #     user_move = rand_bot(count_game)
        # else:
        #     user_move = randint(1, 28)
        # print('Компьютер забрал:', user_move, 'конфет')
        # count_player = 0

    count_game -= user_move
    sleep(1)
    print('Остаток конфет:', count_game)
    sleep(1)
    if count_game < 29:
        print('Победил игрок: ', players_list[count_player])
        break


# 3. Создайте программу для игры в ""Крестики-нолики"".

board = range(1, 10)
board = list(board)
def board_game(board):
    count = 1
    for i in range(3):
        print('\t    |     |')
        print('\t', board[0 + i * 3], ' | ', board[1 + i * 3], ' | ', board[2 + i * 3])
        if count < 3:
            print('\t____|_____|____')
            count += 1
    print('\t    |     |')

#user move
def user_move(player_id):
    valid = False
    while not valid:
        player_answer = input('Куда поставить ' + player_id + ': ')
        try:
            player_answer = int(player_answer)
        except:
            print('Не корректный ввод. Это число?')
            continue
        if player_answer >=1 and player_answer <=9:
            if str(board[player_answer - 1]) not in 'XO':
                board[player_answer - 1] = player_id
                valid = True
            else:
                print('Эта клетка занята')
        else:
            print('Чтобы совершить ход введите число от 1 до 9')

def your_win(board):
    win_position = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for position in win_position:
        if board[position[0]] == board[position[0]] == board[position[0]]:
            return board[position[0]]
    return False

counter = 0
win = False

while not win:
    board_game(board)
    if counter % 2 == 0:
        user_move('X')
    else:
        user_move('O')
    counter += 1
    if counter > 4:
        temp = your_win(board)
        if temp:
            print(temp, 'победил!')
            win = True
            break
    if counter == 9:
        print('У вас ничья!')
        break

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#    Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle(data):
    data_encode = ""
    i = 0
    while i < len(data):
        count = 1

        while i + 1 < len(data) and data[i] == data[i + 1]:
            count = count + 1
            i = i + 1

        data_encode += str(count) + data[i]
        i = i + 1

    return data_encode

f_in = open('files/f_in.txt', 'r')
f_out = open('files/f_out.txt', 'w')
f_out.write(rle(f_in.read()))

f_in.close()
f_out.close()