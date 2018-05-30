# coding = utf-8
import random
"""
求一个无序列表，排序后相邻元素的差的最大值 时间复杂度O(N)
"""


def max_difference(list1):
    if list1 is None or len(list1) < 2: 
        return 0
    min_num = min(list1)
    max_num = max(list1)
    length = len(list1)
    # 只存储每个桶的最大值和最小值
    min_list = [0]*(length+1)
    max_list = [0]*(length+1)
    # 当前桶是否有元素
    has_num = [False]*(length+1)
    # 遍历列表元素放入指定桶中
    for x in list1:
        index = get_bucket_index(x, length, min_num, max_num)
        min_list[index] = min(x, min_list[index]) if has_num[index] else x
        max_list[index] = max(x, max_list[index]) if has_num[index] else x
        has_num[index] = True
    # 前一个非空桶的最大值
    larger = 0
    res = 0
    i = 0
    # 找到第一个非空桶
    while i < length+1:
        if has_num[i]:
            larger = max_list[i]
            i += 1
            break
        i += 1
    # 计算当前非空桶的最小值和前一个非空桶的最大值的差值
    while i < length+1:
        if has_num[i]:
            res = max(res, min_list[i] - larger)
            larger = max_list[i]
        i += 1
    return res


def get_bucket_index(num, length, min_num, max_num):
    """
    找到指定元素应放入的桶的序号
    """
    return (num - min_num) * length // (max_num - min_num)


def main():
    list1 = [random.randint(-100,100) for i in range(30)]
    print(list1)
    res = max_difference(list1)
    print(res)


if __name__ == '__main__':
    main()
