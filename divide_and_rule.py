'''Разделяй и властвуй'''


def summ(arg):
    total = 0
    for x in arg:
        total += x
    return total


def rec(arg):
    """Сумма элементов списка"""
    if arg == []:
        return 0
    else:
        return arg[0] + rec(arg[1:])


def count(list):
    """Рекурсивная функция для подсчта элементов в списке."""
    if list == []:
        return 0
    return 1 + count(list[1:])


def max_number(list):
    """Наибольше числов списке."""
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max_number(list[1:])
    return list[0] if list[0] > sub_max else sub_max
