# coding = utf-8
"""
给定一个列表 [1,2,3,4,5,6,7],希望得到新列表[6,7,1,2,3,4,5]
"""

def reverse_list(list1, left, right):
    """
    将list的指定区间的元素进行反转
    """
    if list1 is None or len(list1) <= 1:
        return
    while left <= right:
        list1[left], list1[right] = list1[right], list1[left]
        left += 1
        right -= 1


def main():
    list1 = [1, 2, 3, 4, 5, 6, 7]
    reverse_list(list1, 0, 4)
    reverse_list(list1, 5, 6)
    reverse_list(list1,0,6)
    print(list1)

if __name__ == '__main__':
    main()
