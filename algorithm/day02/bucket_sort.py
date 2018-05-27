# coding = utf-8
import random       
"""
桶排序
对于N个元素，创建N+1个桶，最大数单独放入最后一个桶
比如数据在10-30范围内，有5个数字，创建6个桶
0号桶 [10,14) 1号桶[14,18) 2号桶[18,22)......5号桶[30]
0~(n-1)号桶，每个桶的负责区间大小：（max-min)/n
"""


def insert_sort(list1):
    """
    插入排序
    """
    if list1 is None or len(list1) < 2:
        return
    for i in range(0, len(list1)):
        temp = list1[i]
        j = i
        while j > 0 and list1[j-1] > temp:
            list1[j] = list1[j-1]
            j -= 1
        list1[j] = temp


def bucket_sort(list1):
    """
    桶排序
    """
    if list1 is None or len(list1) < 2:
        return
    min_num = min(list1)
    max_num = max(list1)
    length = len(list1)
    # 产生length+1个桶
    bucket = [[]for i in range(length+1)]
    # 遍历列表元素放入桶中
    for x in list1:
        index = get_bucket_index(x, length, min_num, max_num)
        bucket[index].append(x)
    # 每个桶的内部元素进行排序
    for i in range(len(bucket)):
        insert_sort(bucket[i])

    list1.clear()
    for x in bucket:
        list1.extend(x)


def get_bucket_index(num, length, min_num, max_num):
    """
    找到指定元素应放入的桶的序号
    """
    return (num - min_num) * length // (max_num - min_num)


def main():
    list1 = [random.randint(-100,100) for i in range(30)]
    print(list1)
    bucket_sort(list1)
    print(list1)


if __name__ == '__main__':
    main()
