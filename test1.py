# В коробке лежат другие коробки, а в них лежат маленькие коробочки.
# Ключ находится где-то там. Какой алгоритм поиска ключа предложите вы?
# Подумайте над алгоритмом, прежде чем продолжить чтение.

def look_for_key(main_box):  # ищи ключ(основной бокс)
    pile = main_box.make_a_pile_to_lok_through()  # основной ящик сделать кучу, чтобы пройти через
    while pile is not empty:  # куча пустая
        box = pile.grab_a_box()  # куча возьми коробку
        for item in box():  # предмет коробка
            if item.is_a_box():  # предмет - это коробка
                pile.append(item)  # куда добавить предмет
            elif item.is_a_key():  # предмет - это ключ
                print('нашел ключ')


# рекурсия
def look_for_keys(box):
    for item in box:
        if item.is_a_box():  # предмет - это коробка
            look_for_keys(item)
        elif item.is_a_key():
            print('Ключ найден')


def countdown(i):  # обратный отсчет
    while True:
        i -= 1
        if i == -100:
            break
        print(i)


def countdown1(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i)


countdown1(4)
