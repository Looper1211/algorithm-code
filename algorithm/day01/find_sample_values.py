# coding = utf-8
"""
两个有序列表中打印相同值
"""


def find_sample_values(list1,list2):
    """
    两个有序列表中打印相同值
    """
    if list1 is None or len(list1) < 1:
        return
    if list2 is None or len(list2) < 1:
        return
    p1 = 0
    p2 = 0
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] < list2[p2]:
            p1 += 1
        elif list1[p1] > list2[p2]:
            p2 += 1
        else:
            print(list1[p1], end=" ")
            p1 += 1
            p2 += 1
