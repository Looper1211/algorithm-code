# coding = utf-8
"""
经典快速排序
"""

def swap(list1, x, y):
    """
    对于列表中指定位置的元素进行交换
    """
    list1[x], list1[y] = list1[y], list1[x]


def sort(list1):
    if list1 is None or len(list1) < 2:
        return
    quick_sort(list1, 0, len(list1) - 1)


def quick_sort(list1, left, right):
    """
    快速排序
    """
    if left < right:
        # 默认选择区间最右边的元素进行划分
        part = partition(list1, left, right, list1[right])
        quick_sort(list1, left, part[0] - 1)
        quick_sort(list1, part[1] + 1, right)


def partition(list1, left, right, key):
    """
    根据key，对list1在[left,right]区间上的元素进行划分
    """
    less = left - 1
    more = right + 1
    index = left
    while index < more:
        if list1[index] < key:
            swap(list1, less + 1, index)
            less += 1
            index += 1
        elif list1[index] > key:
            swap(list1, more - 1, index)
            more -= 1
        else:
            index += 1
    # 返回等于区的区间位置
    return less + 1, more - 1


def main():
    list1 = [2, 1, 4, 5, 8, 1, 7, 3, 6]
    sort(list1)
    print(list1)


if __name__ == '__main__':
    main()
