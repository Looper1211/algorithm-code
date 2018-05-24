# coding = utf-8


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


def main():
    list1 = [1, 5, 2, 3, 4]
    insert_sort(list1)
    print(list1)


if __name__ == '__main__':
    main()
