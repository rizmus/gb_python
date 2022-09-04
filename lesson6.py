#----list comprehension

d = 0.001
print('Задача №1\nЗаданная точность d =', d)
from decimal import Decimal
d = int(Decimal(str(d)).as_tuple().exponent*(-1))

steps = 1000000
pi = sum((-1.0)**n / (2.0*n+1.0) for n in reversed(range(steps))) * 4
print('Число π с точностью d:', round(pi, d))

#----enumerate

number_list = [2, 3, 5, 9, 3]
value = 0

for index, item in enumerate(number_list):
    if index % 2 != 0:
        value += item
print('Ответ к задаче №1: ', value)

#----lambda

f = open('text.txt', 'w')

text_value = input('Введите текст где необходимо убрать авб:\n')
text_abv = ' '.join(filter(lambda x: 'абв' not in x, text_value.split()))

f.write(text_abv)
f.close()

#----