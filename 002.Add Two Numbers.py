# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = ListNode(0)
        result_pointer = result

        while (l1 or l2):
            sum = 0
            if (l1):
                sum = l1.val
                l1 = l1.next
            if (l2):
                sum += l2.val
                l2 = l2.next
            sum += carry
            result_pointer.next = ListNode(sum % 10)
            result_pointer = result_pointer.next
            carry = (sum >= 10)
        if (carry):
            result_pointer.next = ListNode(1)
        result_pointer = result.next
        del result
        return result_pointer
