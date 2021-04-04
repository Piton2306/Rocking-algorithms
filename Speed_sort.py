def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


x = [2, 4, 6, 9, 2]


def print_items(list):
    for items in list:
        print(items)


from time import sleep


def print_item_sleep(list):
    for items in list:
        sleep(1)

        print(items,end=',')
print_item_sleep(x)
