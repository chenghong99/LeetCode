# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """

        prev = fix = ListNode(0, head)

        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next ## curr = 2
        for i in range(right - left):
            temp = curr.next ## temp = 3
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        
        return fix.next