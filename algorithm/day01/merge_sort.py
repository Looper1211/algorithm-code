# coding = utf-8
"""
归并排序--分治思想
"""


def sort(list1):
    if list1 is None or len(list1) < 2:
        return
    merge_sort(list1, 0, len(list1)-1)


def merge_sort(list1, left, right):
    """
    归并排序,采用 分治思想，先让左半边和右半边分别有序,再合并
    """
    if left < right:
        mid = (left+right) >> 1
        merge_sort(list1, left, mid)
        merge_sort(list1, mid+1, right)
        merge(list1, left, mid, right)


def merge(list1, left, mid, right):
    """
    两个有序区间合并为一个大区间
    """
    temp = []
    p1 = left
    p2 = mid+1

    while p1 <= mid and p2 <= right:
        if list1[p1] <= list1[p2]:
            temp.append(list1[p1])
            p1 += 1
        else:
            temp.append(list1[p2])
            p2 += 1

    while p1 <= mid:
        temp.append(list1[p1])
        p1 += 1

    while p2 <= right:
        temp.append(list1[p2])
        p2 += 1

    for i in range(0, len(temp)):
        list1[left+i] = temp[i]


def main():
    list1 = [1, 3, 1, 81, 7, 2, 5, 9]
    sort(list1)
    print(list1)


if __name__ == '__main__':
    main()
