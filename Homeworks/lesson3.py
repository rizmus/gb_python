# Задача №1
number_list = [2, 3, 5, 9, 3]
value = 0

for index, item in enumerate(number_list):
    if index % 2 != 0:
        value += item
print('Ответ к задаче №1: ', value)



# Задача №2
list_w2 = [2, 3, 4, 5, 6]
list_sum = []
a = 0
b = len(list_w2) - 1

while a <= b:
    c = list_w2[a] * list_w2[b]
    a += 1
    b -= 1
    list_sum.append(c)
print('Ответ к задаче №2:', list_sum)

# Задача №3
import math

list_w3 = [1.1, 1.2, 3.1, 5, 10.01]
x = 0
num_max = 0
num_min = list_w3[0] % 1

for i in list_w3:
    value_temp = math.modf(i)
    if value_temp[0] > num_max:
        num_max = value_temp[0]
    if value_temp[0] < num_min and value_temp[0] > 0:
        num_min = value_temp[0]

print('Ответ к задаче №3:', round(num_max - num_min, 2))

#Задача 4
num_list_w4 = []
num_w4 = int(input('Задача №4. Введите десятичное число: '))

while num_w4 != 0:
    if num_w4 % 2 == 0:
        num_list_w4.append(0)
        num_w4 = num_w4 // 2
    else:
        num_list_w4.append(1)
        num_w4 = (num_w4 - 1) // 2
print('Ответ к задаче №4:', ''.join(map(str, num_list_w4)))

#Задача №5


num_w5 = int(input('Задача №5. Введите число: '))
num_list_w5 = [0, 1]
num_list_w5_rev = []
f = 2
if num_w5 > 0:
    while f != num_w5 + 1:
        num_list_w5.append(num_list_w5[f-1] + num_list_w5[f-2])
        f += 1
    for i in num_list_w5:
        if i > 0:
            num_list_w5_rev.append(i * -1)
    num_list_w5_rev.reverse()
    list_result = num_list_w5_rev + num_list_w5
    print('Ответ к задаче №5: ', list_result)
else:
    print('Что-то пошло не так :)')