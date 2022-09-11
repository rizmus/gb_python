# Инициализация пользователя
def user_initiation(email):
    user_current = []
    with open('users.txt', 'r') as file:
        for line in file:
            if email in line:
                user_current = line.split(' | ')
                return user_current[2]


# Инициализация словаря
def file_initiation(filename):
    task_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            val = line.split('|')
            for index, item in enumerate(val):
                task_dict[val[0]] = item
    return task_dict

file_initiation('roman.txt')