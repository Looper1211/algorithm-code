# coding = utf-8
"""
判断链表是否有环 leetcode 141
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False