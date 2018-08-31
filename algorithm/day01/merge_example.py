# coding = utf-8
"""
小和问题
例如，数组s=[1,3,5,2,4,6]，在s[0]的左边小于等于s[0]的数的和为0，在s[1]的左边小于或等于s[1]的数和为1，
在s[2]的左边小于等于s[2]的数和为1+3=4…以次类推，所以s的小和为0+1+4+1+6+15=27，
给定一个数组，实现函数返回小和

逆序对问题
在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。给你一个数组，求出这个数组中逆序对的总数。
概括：如果a[i] > a[j] 且 i < j， a[i] 和 a[j] 构成一个逆序对。如：序列 [2, 4, 1, 3, 5] 中，
有 3 个逆序对 (2, 1), (4, 1), (4, 3)，则返回 3 。
"""


def sort(list1):
    """
    借用归并排序思想
    """
    if list1 is None or len(list1) < 2:
        return
    return merge_sort(list1, 0, len(list1)-1)


def merge_sort(list1, left, right):
    """
    分治思想，先让左半边和右半边分别有序,再合并
    """
    if left == right:
        return 0
    mid = (left + right) >> 1
    return merge_sort(list1, left, mid) + merge_sort(list1, mid + 1, right) + merge(list1, left, mid, right)


def merge(list1, left, mid, right):
    """
    两个有序区间合并为一个大区间
    """
    temp = []
    p1 = left
    p2 = mid+1
    ans = 0

    while p1 <= mid and p2 <= right:
        if list1[p1] < list1[p2]:
            # 小和问题
            # ans += list1[p1] * (right - p2 + 1)
            temp.append(list1[p1])
            p1 += 1
        else:
            # 逆序对问题
            # ans += (mid - p1 + 1)
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

    return ans


def main():
    list1 = [1, 3, 5, 2, 4, 6]
    ans = sort(list1)
    print(ans)

if __name__ == '__main__':
    main()
