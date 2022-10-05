# Модуль для создания списков(изменяемые), кортежей(не изменяемы), словарей(изменяемые по ключу)


def Int_list_create():
    int_list = list(map(int,input('введите целые числа через пробел ').split()))
    return int_list


def Float_list_create():
    float_list = list(map(float,input('введите вещественные числа через пробел ').split()))
    return float_list

def Any_range_list():
    n1 = int(input('Введите начльное значение:'))
    n2 = int(input('Введите конечно значение:'))
    any_range_list = list(range(n1,n2))
    return any_range_list

# def Find_double()
#
#     new_list = Int_list_create()
#     new_list1 = []
#
#     for x in new_list:
#         if new_list.count(x) == 1: # если повторение больше или равно 1
#             new_list1.append(x)
#
#     return new_list, new_list1

