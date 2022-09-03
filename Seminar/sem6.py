# #---
#
# for number in map(lambda x: x**2, range(10)):
#     print(number)
#
# #---
#
# for number in filter(lambda x: x % 5 == 0, range(50)):
#     print(number)
#
# #---
#
# a = filter(lambda x: x % 5 == 0, range(50))
#
# print('---1---')
# for n in a:
#     print(n)
#
# print('---2---')
# for n in a:
#     print(n)
#
# #---
#
# a = filter(lambda x: x % 5 == 0, range(50))
#
# b = next(a)
# c = next(a)
#
# print('--', b)
# print('--', c)
#
# for n in a:
#     print(n)
#
# #---
#
# def f():
#     for n in range(10):
#         return n
# print(f())
#
# #---
#
# def f():
#     for n in range(10):
#         yield n
#
# a = f()
#
# # print(next(a))
# # print(next(a))
# # print(next(a))
#
# for item in a:
#     print(item)
# #---
# # range для вещественных чисел
# def my_range (start, stop=None, step=1):
#     if stop is None:
#         stop = start
#         start = 0
#     while start < stop:
#         yield start
#         start += step
#
#
# i = 0
# for n in my_range(5, 10, -2):
#     print(n)
#     i +=1
#     if i == 20:
#         break
#
# print('---')
# for n in range(5, 10, -2):
#     print(n)


val = '1+2*3/4'.replace(' ', '')
num_list = []
numbers = []
tmp = 1
next_true = False

for i in range(len(val)):
    if next_true:
        next_true = False
        continue
    if val[i].isdigit():
        numbers.append(int(val[i]) * tmp)
    elif val[i] == '-':
        tmp = -1
    elif val[i] == '+':
        tmp = 1
    elif val[i] == '*':
        numbers[-1] *= int(val[i+1])
        next_true = True
    elif val[i] == '/':
        numbers[-1] /= int(val[i+1])
        next_true = True


print(sum(numbers))
