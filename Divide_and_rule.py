def summ(arg):
    total = 0
    for x in arg:
        total += x
    return total


# Напишите код для функции sum
def rec(arg):
    if arg == []:
        return 0
    else:
        return arg[0] + rec(arg[1:])


# Напишите рекурсивную функцию для подсчета элементов в списке.
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


# Найдите наибольшее число в списке.
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max


print(max([1, 5, 56, 7, 7]))
