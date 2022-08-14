# Задача 1
# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

print('Задача 1')
number = int(input('Введите день недели от 1 до 7: '))

if number == 6 or number == 7:
    print('Да, это выходной день')
elif number >= 1 and number < 6:
    print("Нет, это будний день")
else:
    print('Вы ввели число в неверном диапазоне')


# Задача 2
# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Задача 2')
for x in range(2):
    for y in range(2):
        for z in range(2):
          print (f'{x} | {y} | {z} {int (not (x or y or z))} {int (not x and not y and not z)}')


# Задача 3
# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).
#
# x>0 y>0 - 1 x>0 y<0 - 2 x<0 y<0 - 3 x<0 y>0 4

print('Задача 3')
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

# Задача 4
# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

print('Задача 4')
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

print('Задача 5')
import math

a = []
b = []

a.append(float(input('Введите координату Xa: ')))
a.append(float(input('Введите координату Ya: ')))
b.append(float(input('Введите координату Xb: ')))
b.append(float(input('Введите координату Yb: ')))

distanse = math.sqrt(((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2))

print('Координаты точки A: ', a)
print('Координаты точки B: ', b)
print('Длина между точками A и B: ', distanse)


