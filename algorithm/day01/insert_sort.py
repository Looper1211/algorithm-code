# coding = utf-8


def insert_sort(list1):
    """
    插入排序
    """
    for i in range(1, len(list1)):
        temp = list1[i]
        j = i - 1
        while j >= 0 and temp < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = temp


def insert_sort2(list1):
    if list1 is None or len(list1) < 2:
        return
    
    for i in range(1, len(list1)):
        for j in range(i - 1, -1, -1):
            if list1[j] > list1[j + 1]:
                swap(list1, j, j + 1)
            else:
                break

def swap(list1, x, y):
    """
    对于列表中指定位置的元素进行交换
    """
    list1[x], list1[y] = list1[y], list1[x]


def main():
    list1 = [5, 2, 3, 4, 1]
    insert_sort2(list1)
    print(list1)


if __name__ == '__main__':
    main()
