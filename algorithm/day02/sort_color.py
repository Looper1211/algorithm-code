# coding = utf-8
"""
荷兰国旗问题
荷兰国旗有三横条块构成，自上到下的三条块颜色依次为红、白、蓝。现有若干由红(0)、白(1)、蓝(2)三种颜色的条块序列，
要将它们重新排列使所有相同颜色的条块在一起。
要求将所有红色的条块放最左边、所有白色的条块放中间、所有蓝色的条块放最右边。
01021021010 -> 0000111122
"""


def swap(list1, x, y):
    """
    对于列表中指定位置的元素进行交换
    """
    list1[x], list1[y] = list1[y], list1[x]


def sort_color(list1):
    # 小于区的标记
    less = -1
    # 大于区的标记
    more = len(list1)
    idx = 0
    while idx < more:
        # 当前元素小于1
        if list1[idx] < 1:
            # 小于区扩大一个位置
            less += 1
            swap(list1, less, idx)
            idx += 1
        # 当前元素 大于 1
        elif list1[idx] > 1:
            # 大于区扩大一个位置
            more -= 1
            swap(list1, more, idx)
        else:
            idx += 1


def main():
    list1 = [0, 1, 0, 2, 1, 0, 2, 1, 0, 1, 0]
    sort_color(list1)
    print(list1)


if __name__ == '__main__':
    main()
