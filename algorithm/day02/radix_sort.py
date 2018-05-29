# coding = utf-8
import random
"""
基数排序 时间复杂度 o(d(n+r)) 其中，d 为位数，r 为基数，n 为原数组个数。 
"""

def radix_sort(list1, radix):
    if list1 is None or len(list1) < 2:
        return
    # 计算最大位数
    d = max([len(str(x)) for x in list1])
    #  根据进制数创建对应数量的桶
    buckets = [[]for i in range(radix)]
    rate = 1
    i = 0
    while i < d:
        # 每个通进行初始化清理元素
        for j in range(radix):
            buckets[j].clear()
        # 遍历列表元素，放入指定桶中
        for x in list1:
            index = (x//rate) % 10
            buckets[index].append(x)
        list1.clear()
        for x in buckets:
            list1.extend(x)
        rate *= 10
        i += 1


def main():
    list1 = [random.randint(1, 1000) for i in range(30)]
    print(list1)
    radix_sort(list1, 10)
    print(list1)


if __name__ == '__main__':
    main()
