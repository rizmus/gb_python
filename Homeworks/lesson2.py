
# Напишите программу, которая принимает на вход число N и выдает последовательность из N элементов


a = int(input())
n = 1
for i in range(a):
    print(n)
    n *= -3


a = input()
b = input()

if len(a) > len(b):
    print('Строка А')
elif len(a) < len(b):
    print('Cтрока Б')
else:
    print('Строки равны')