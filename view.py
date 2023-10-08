# функции для работы с пользователем

def select_op():
    op = int(input('выбери, что хочешь сделать:\n1 - новая запись\n2 - поиск записи\n3 - все записи\n'
                   '4 - удалить запись\n5 - редактировать запись\n0 - выход\n'))
    return op


def get_info():
    l_name = input('введи фамилию: ')
    f_name = input('введи имя: ')
    tel = input('введи телефон: ')
    data = l_name + ';' + f_name + ';' + tel + '\n'
    return data


def get_string(arg):
    search_info = input(arg)
    return search_info
