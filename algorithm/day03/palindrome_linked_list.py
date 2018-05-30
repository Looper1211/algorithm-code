# coding = utf-8
"""
判断一个单向链表是否是回文链表，进阶：要求O（n）的时间复杂度和O（1）的空间复杂度。 leetcode 234

算法有以下几种：
1、遍历整个链表，将链表每个节点的值记录在列表中，再判断列表是不是一个回文列表，
    时间复杂度为O（n），但空间复杂度也为O（n)。

2、反转链表法，将链表后半段原地翻转，再将前半段、后半段依次比较，判断是否相等，
    时间复杂度O（n），空间复杂度为O（1）。

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def isPalindrome(self, head):
#         """
#         :type head: ListNode
#         :rtype: bool
#         """
#         list1 = []
#         while head:
#             list1.append(head.val)
#             head = head.next
#         return list1 == list1[::-1]

class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 前一个
        pre = None
        # 新的链表头
        new_head = None
        p = head
        while p:
            # 找出当前结点的下一个结点
            next_node = p.next
            # 如果下一个结点是None，该结点就是新的链表头
            if not next_node:
                new_head = p
            # 当前结点的下一个指向前一个结点
            p.next = pre
            # 前一个结点变为当前结点
            pre = p
            # 当前结点变为下一个结点
            p = next_node
        return new_head
        
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while fast and fast.next:
            fast =  fast.next.next
            slow = slow.next
        # 奇数个结点    
        if fast:
            slow.next = self.reverseList(slow.next)
            slow = slow.next
        # 偶数个结点
        else:
            slow = self.reverseList(slow)
        # 前半段和后半段依次比较
        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True