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

        while fast != None:
            if fast.next != None and fast.next.next != None:
                fast = fast.next.next
                slow = slow.next
            else:
                return None
            if fast == slow:
                break
        while head != slow:
            head = head.next
            slow = slow.next
        return head            



        