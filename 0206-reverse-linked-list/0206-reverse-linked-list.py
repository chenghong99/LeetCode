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
        ## 1 -> 2 -> 3 -> 4 -> 5
        ## None <- 1  2 -> 3 -> 4 -> 5
        ## 1 <- 2 -> 3 -> 4 -> 5
        ## 1 <- 2 <- 3 -> 4 -> 5
        ## I need 3 reference 
        
        prev = None
        
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp 

        return prev

