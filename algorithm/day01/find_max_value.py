# coding = utf-8


def find_max_value(list1):
    """
    找出列表中的最大值
    """
    if list1 is None or len(list1) < 1:
        return None
    max_num = list1[0]
    i = 1
    while i < len(list1):
        if list1[i] > max_num:
            max_num = list1[i]
        i += 1
    return max_num


def find_max_value2(list1, left, right):
    """
    递归版 查找列表中的最大值
    """
    if left == right:
        return list1[left]
    mid = (left + right) >> 1
    # 找出左半部分最大值
    max_num1 = find_max_value2(list1, left, mid)
    # 找出右半部分最大值
    max_num2 = find_max_value2(list1, mid + 1, right)
    # 返回最大值
    return max(max_num1, max_num2)


if __name__ == '__main__':
    list1 = [1, 3, 5, 1, 4]
    ans = find_max_value2(list1, 0, len(list1) - 1)
    print(ans)
