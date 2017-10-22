# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        pre = head
        cur = head.next
        while cur:
            if pre.val == cur.val:
                cur = cur.next
                del pre.next
                pre.next = cur
            else:
                pre = cur
                cur = cur.next
        return head
