# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        left = head
        mid = head 
        right = None
        
        while mid != None:
            left = mid.next 
            mid.next = right
            right = mid
            mid = left 
            
        head=right
        return head
    
    