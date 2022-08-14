# a = 25
# b = 3.5
# c = a + b
#
# print(type(a))
# print(type(b))
# print(type(c))
#
# print(c)
#
# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
#
# if a ** 2 == b or b ** 2 ==a:
#     print('да')
# else:
#     print('нет')

# max_ = float('-inf')
#
# for i in range(5):
#     value = int(input())
#     if value > max_:
#         max_ = value
# print(max_)

# number = int(input())
# start = -number
#
# while start <= number:
#     print(start, end=' ')
#     start += 1

# s = '21451.21521521'
# print(s.split('.')[1][0])
# last = None
#
# for i in s:
#     if last == '.':
#         print(i)
#     last = i
#
#
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(x, y, z, 'формула для 2ой задачи дз')
#
#

# # Задача 1
# # Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# # и проверяет, является ли этот день выходным.

number = int(input('Введите день недели от 1 до 7: '))

if number == 6 or number == 7:
    print('Да, это выходной день')
elif number >= 1 and number < 6:
    print("Нет, это будний день")
else:
    print('Вы ввели число в неверном диапазоне')


# # Задача 2
# # Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, z, 'формула для 2ой задачи дз')


# # Задача 3
# # Напишите программу, которая принимает на вход координаты точки (X и Y),
# # причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# # эта точка (или на какой оси она находится).
#
# # x>0 y>0 - 1 x>0 y<0 - 2 x<0 y<0 - 3 x<0 y>0 4

x = float(input('Введите коородинату x: '))
y = float(input('Введите коородинату y: '))

if x>0 and y>0:
    print('Четверть 1')
elif x>0 and y<0:
    print('Четверть 2')
elif x<0 and y<0:
    print('Четверть 3')
elif x<0 and y>0:
    print('Четверть 4')
else:
    print('В координатах введен 0')

# # Задача 4
# # Напишите программу, которая по заданному номеру четверти,
# # показывает диапазон возможных координат точек в этой четверти (x и y).
#
quarter = int(input('Введите четверть от 1 до 4: '))

if quarter == 1:
    print('Возможные координаты точек:\n X>0, Y>0')
elif quarter == 2:
    print('Возможные координаты точек:\n X>0, Y<0')
elif quarter == 3:
    print('Возможные координаты точек:\n X<0, Y<0')
elif quarter == 4:
    print('Возможные координаты точек:\n X<0, Y>0')
else:
    print('Введено число <0 or >4')

# Задача 5
# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
import math

a = [43, -273]
b = [-234, 93]

distanse = math.sqrt(((b[0] - a[0]) ** 2) + ((b[1] - b[1]) ** 2))

print('Координаты точки A: ', a)
print('Координаты точки B: ', b)
print('Длина между точками A и B: ', distanse)


