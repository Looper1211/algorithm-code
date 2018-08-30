# coding = utf-8


def buddle_sort(list1):
    """
    冒泡排序
    """
    if list1 is None or len(list1) <= 1:
        return
    for end in range(len(list1) - 1, 0, -1):
        for j in range(0, end):
            if list1[j] > list1[j + 1]:
                swap(list1, j, j + 1)


def swap(list1, x, y):
    """
    对于列表中指定位置的元素进行交换
    """
    list1[x], list1[y] = list1[y], list1[x]


if __name__ == '__main__':
    list1 = [2, 1, 3, 8, 4]
    buddle_sort(list1)
    print(list1)
