#функции для работы с базой данных


def edit_info(num_e, data):
    del_info(num_e)
    with open('data.txt', encoding='utf-8') as file:
        lst = file.readlines()
        lst.insert(int(num_e), data)
    with open('data.txt', 'w', encoding='utf-8') as file:
        file.writelines(lst)

def del_info(num_d):
    with open('data.txt', encoding='utf-8') as file:
        lst = file.readlines()
        lst.pop(int(num_d))
    with open('data.txt', 'w', encoding='utf-8') as file:
        file.writelines(lst)

def write_info(human_info):
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(human_info)

def search_info(arg):
    with open('data.txt', 'r', encoding='utf-8') as file:
        lst = file.readlines()
        res = []
        for i in range(len(lst)):
            if arg in lst[i]:
                res.append(lst[i])
                lst[i] = lst[i].strip()
                print(f'{i}. {lst[i]}')
        return res

def book_view():
    with open('data.txt', encoding='utf-8') as file:
        lst = file.readlines()
        for i in range(len(lst)):
            lst[i]=lst[i].strip()
            print(f'{i}. {lst[i]}')