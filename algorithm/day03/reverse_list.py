# coding = utf-8
"""
反转链表 leetcode 206
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
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