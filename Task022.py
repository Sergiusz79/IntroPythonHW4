# Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def enter_num(text):
    try:
        a = int(input(f"Enter the {text}: \n"))
    except:
        print("Error! This is not integer number!")
    return a

def create_sort_list(n, text):
    list_1 = [enter_num(text) for i in range(n)]
    list_1.sort()
    return list_1


def interselection(list_1, list_2):
    set(list_1, list_2)
    a = list_1.intersection(list_2)
    return a


def task():
    n = enter_num('number of list items')
    m = enter_num('number of list items')
    list_1 = create_sort_list(n, 'list_1 item')
    list_2 = create_sort_list(m, 'list_2 item')
    a = interselection(list_1, list_2)
    print(a)


task()


