# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

value = input('Задача №1\nВведите вещественное число: ')
sum = int(0)

if is_number(value) == True:
    for i in value:
        if i != '.':
            sum += int(i)
    print('Ответ к задаче №1:', sum)
else:
    print ('Введено не число')



# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n_num = int(input('\nЗадача №2\nВведите число N: '))
result_n = 1
for i in range(1, n_num + 1):
    result_n *= i
    print(result_n)


# Задайте список из n чисел последовательности (1+1/n)^n и
# выведите на экран их сумму, округлённую до трёх знаков после точки.


n_num3 = int(input('\nЗадача №3\nВведите число N: '))
result_h3 = 0

for i in range(1, n_num3 + 1):
    result_h3 += ((1+1/i)**i)
print('Результат по задаче №3:', round(result_h3, 3))

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры через пробел.

n_for_list, a_position, b_position = input('\nЗадача №4\nВведите через проблел N, a и b: ').split()

n_for_list = int(n_for_list)
a_position = int(a_position)
b_position = int(b_position)

list = []

result_h4 = 0
for i in range(-n_for_list, n_for_list + 1):
    list.append(i)
result_h4 = list[a_position] * list[b_position]
print('Список [-N, N] элементов:', list, '\nЧисло A: ', a_position, '\nЧисло B: ', b_position)
print('Произведение элементов A и B: ', result_h4)


# Реализуйте алгоритм перемешивания списка.

import random

list_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('\nЗадача 5\nИзначальный список:', list_a)
random.shuffle(list_a)
print('Список после перемешивания:', list_a)