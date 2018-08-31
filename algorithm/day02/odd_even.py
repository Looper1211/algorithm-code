"""
把列表元素按照奇数和偶数进行划分，要求空间复杂度 O(1),时间复杂度O(N)
"""


def swap(list1, x, y):
    """
    对于列表中指定位置的元素进行交换
    """
    list1[x], list1[y] = list1[y], list1[x]


def partation2(list1, L, R):
    more = R + 1
    cur = L
    while cur < more:
        if list1[cur] % 2 == 0:
            swap(list1, more - 1, cur)
            more -= 1
        else:
            cur += 1


def partation(list1, L, R):
    less = L - 1
    cur = L
    while cur < R:
        if list1[cur] % 2 == 1:
            swap(list1, less + 1, cur)
            less += 1
        cur += 1


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6]
    partation(list1, 0, len(list1) - 1)
    print(list1)
