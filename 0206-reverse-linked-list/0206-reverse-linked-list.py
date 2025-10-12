# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ## need 3 variables to keep track. add a temp head to first head to create prev. 
        prev = None 

        while head:
            curr = head
            head = head.next 
            curr.next = prev 
            prev = curr

        return prev