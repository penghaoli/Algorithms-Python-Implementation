# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 反转链表
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
