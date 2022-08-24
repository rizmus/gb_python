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
print('Задача №3\nВывод неповторяющихся чисел спсика:', list_uniq)

# Задача 4
# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
f = open('polynomial.txt', 'w')

k = int(input('Задача №4\nВведите натуральную степень k: '))
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
for num in list_w4:
    polynomial += str(num)
print('Вывод сгенерированного многочлена: ', polynomial)
f.write(polynomial)
f.close()

# Задача 5
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
import re

f1 = open('polynomial1.txt', 'r')
str1 = f1.read()
f1.close()

f2 = open('polynomial2.txt', 'r')
str2 = f2.read()
f2.close()

polynomial1_list = []
polynomial2_list = []
sum_d = {}
sum_d2 = {}
sum_d_list = []

polynomial1_list = str1.split(sep=' + ')
polynomial2_list = str2.split(sep=' + ')

print('Задача №5')


polynomial1_list.reverse()
polynomial2_list.reverse()

# Первый список
sum_d[0] = polynomial1_list[0] # num
xz = re.findall('[0-9]+', polynomial1_list[1]) #num x
sum_d[1] = xz[0]

for index, item in enumerate(polynomial1_list):
    if index > 1:
        xz = re.findall('[0-9]+', polynomial1_list[index])
        sum_d[int(xz[1])] = xz[0]

# Второй список
sum_d2[0] = polynomial2_list[0] # num
xz = re.findall('[0-9]+', polynomial2_list[1]) #num x
sum_d2[1] = xz[0]

for index, item in enumerate(polynomial2_list):
    if index > 1:
        xz = re.findall('[0-9]+', polynomial2_list[index])
        sum_d2[int(xz[1])] = xz[0]

# Суммируем значения в словаре

if len(sum_d) >= len (sum_d2):
    for i in range(0, len(sum_d)):
        if i <= len(sum_d2) - 1:
            sum_d_list.append(int(sum_d[i]) + int(sum_d2[i]))
        else:
            sum_d_list.append(sum_d[i])
else:
    for i in range(0, len(sum_d2)):
        if i <= len(sum_d) - 1:
            sum_d_list.append(int(sum_d[i]) + int(sum_d2[i]))
        else:
            sum_d_list.append(sum_d2[i])

#Собираем многочлен и отправляем в файл:
list_w5 = []
count = 2
for i in range(1, len(sum_d_list)):
    if i == 1:
        list_w5.append(str(sum_d_list[0]))
        list_w5.append(str(sum_d_list[1]) + 'x' + ' + ')
    else:
        list_w5.append(str(sum_d_list[i]) + 'x**' + str(count) + ' + ')
        count += 1

list_w5.reverse()

# Делаем строку и отправляем в файл

f_sum = open('polynomial_sum.txt', 'w')

polynomial_sum = ''

for num in list_w5:
    polynomial_sum += str(num)
print('Вывод суммы многочленов: ', polynomial_sum)
f_sum.write(polynomial_sum)
f_sum.close()

