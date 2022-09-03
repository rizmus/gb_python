def chek_num(value):
    value = value.replace(',', '.', 1)
    try:
        float(value)
        return value
    except:
        return False


def chek_operator(operator):
    return operator



a = chek_num(input('Введите первое значение: '))
b = chek_num(input('Введите второе значение: '))
operator = chek_operator(input('Какое арифметическое действие совершить: '))
print(a, b, operator)
