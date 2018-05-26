# coding = utf-8
"""
求无序列表中第K大元素，要求时间复杂度o(n)，空间复杂度o(1)
"""


def kth_largest_element(list1, k):
    """
    求列表第k大元素的值
    """
    if list1 is None or len(list1) < 1 or k > len(list1):
        return None
    return quick_sort(list1, 0, len(list1)-1, k)


def swap(list1, x, y):
    """
    对于列表中指定位置的元素进行交换
    """
    list1[x], list1[y] = list1[y], list1[x]


def quick_sort(list1, left, right, k):
    """
    利用快排的思想，选择一个数进行划分，将数组化分为区间 list_a(小于等于区) 和 list_b（大于区）,计算出list_a的区间长度len_a
        1. 如果len_a > k,那就在list_a区间再进行划分
        2. 如果llen_a < k,那就在arr_b的区间找第 k - len_a 大元素
        3. 如果 len_a = k，这个就是我们要找的数字
    """
    if left <= right:
        # 默认选择区间最右边的元素进行划分
        part = partition(list1, left, right, list1[right])
        if part[1] == k:
            return list1[part[0]]
        elif part[1] > k:
            return quick_sort(list1, left, part[0]-1, k)
        else:
            return quick_sort(list1, part[0]+1, right, k-part[1])


def partition(list1, left, right, key):
    """
    根据key，对list1在[left,right]区间上的元素进行划分
    """
    less = left - 1
    more = right + 1
    index = left
    while index < more:
        if list1[index] < key:
            less += 1
            swap(list1, less, index)
            index += 1
        elif list1[index] > key:
            more -= 1
            swap(list1, more, index)
        else:
            index += 1
    # 返回小于等于区的末端位置，小于等于区的个数
    return more-1, more-left


def main():
    list1 = [1, 2, 6, 4, 5, 3]
    ret = kth_largest_element(list1, 5)
    print(ret)


if __name__ == '__main__':
    main()
