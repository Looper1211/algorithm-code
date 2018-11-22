# coding = utf-8
"""
在一个有序序列中找到指定元素，找到返回其在序列中的位置，没找到返回-1
"""


def binary_search(list1, k):
    """
    折半（二分）查找
    """
    if list1 is None or len(list1) < 1:
        return -1
    left = 0
    right = len(list1) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if list1[mid] > k:
            right = mid - 1
        elif list1[mid] < k:
            left = mid + 1
        else:
            return mid
    return -1


def binary_search2(list1, left, right, k):
    """
    递归版 二分查找
    """
    # 区间上只有一个数
    if left == right:
        return left if list1[left] == k else -1
    # 划分区间
    mid = (right + left) >> 1
    # 如果中间值 > 目标值，在左半边继续查找
    if list1[mid] > k:
        return binary_search2(list1, left, mid - 1, k)
    # 如果中间值 < 目标值，在右半边继续查找
    elif list1[mid] < k:
        return binary_search2(list1, mid + 1, right, k)
    # 返回值
    else:
        return mid
