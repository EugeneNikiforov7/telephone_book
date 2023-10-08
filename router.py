# связь между view и db

from view import *
from db import *


def main():
    while True:
        ans = select_op()
        if ans == 1:
            write_info(get_info())
        if ans == 2:
            search_info(get_string('Введите строку поиска: '))
        if ans == 3:
            book_view()
        if ans == 4:
            del_info(get_string('Введите номер удаляемого контакта: '))
        if ans == 5:
            edit_info(get_string('Введите номер изменяемого контакта: '), get_info())
        if ans == 0:
            break


main()
