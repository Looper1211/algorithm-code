# coding = utf-8
"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 None。 leetcode 142
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        has_cycle = False
        while fast and slow and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                has_cycle = True
                break
        if not has_cycle:
            return None
        fast = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow