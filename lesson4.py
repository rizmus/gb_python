# Задача 1
# Вычислить число π c заданной точностью d
# *Пример: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# https://completerepair.ru/kak-vychislit-chislo-pi



# Задача 2
# Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N.

num = int(input('Задача №2\nВведите целое число: '))
count = 2
value = 0
mn_list = []
if num > 0:
    for i in range(num + 1):
        mn_list.append(0)

    mn_list[1] = 1

    for i in range(num):
        value = num
        while value % count == 0:
            mn_list[count] += 1
            value = value / count
        else:
            count += 1

    for index, item in enumerate(mn_list):
        if item > 0:
            print('Множитель:', index,'Повторений:', item)
else:
    print('Упс... Что-то пошло не так ¯\_(ツ)_/¯')

# Задача 3
# Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

list_nums = [1, 5, 8, 15, 15, 20, 20, 14, 16, 15, 25]
list_uniq = []

for i in list_nums:
    if i not in list_uniq:
        list_uniq.append(i)
print('Задача 3\nВывод неповторяющихся чисел спсика:', list_uniq)

# Задача 4
# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
f = open('polynomial.txt', 'w')

k = 5
list_w4 = []
value = 0
count = 2
polynomial = ''

for i in range(1, k + 1):
    value = random.randint(0, 100)
    if i == 1:
        list_w4.append(str(value))
        list_w4.append(str(value) + 'x' + ' + ')
    else:
        list_w4.append(str(value) + 'x**' + str(count) + ' + ')
        count += 1

list_w4.reverse()
print(list_w4)
for num in list_w4:
    polynomial += str(num)
print(polynomial)
f.write(polynomial)
f.close()

# Задача 5
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

f1 = open('polynomial1.txt', 'r')
str1 = f1.read()
f1.close()

f2 = open('polynomial2.txt', 'r')
str2 = f2.read()
f2.close()

polynomial1_list = []
polynomial2_list = []
sum_d = {}

polynomial1_list = str1.split(sep=' + ')
polynomial2_list = str2.split(sep=' + ')

print('первый файл: ', polynomial1_list)
print('второй файл: ', polynomial2_list)




