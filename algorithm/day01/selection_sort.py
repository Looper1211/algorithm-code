def sellecttion_sort(list1):
    """
    选择排序
    :param list1:
    :return:
    """
    if list1 is None or len(list1) <= 1:
        return

    for i in range(0, len(list1)-1):
        min_index = i

        for j in range(i+1, len(list1)):
            if list1[j] < list1[min_index]:
                min_index = j

        swap(list1, i, min_index)


def swap(list1, x, y):
    """
    对于列表中指定位置的元素进行交换
    """
    list1[x], list1[y] = list1[y], list1[x]