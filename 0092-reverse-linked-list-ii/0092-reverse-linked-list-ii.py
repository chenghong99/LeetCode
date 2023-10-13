# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        cur = dummy.next
        

        for i in range(1, left):
            cur = cur.next
            prev = prev.next
            
        perm_prev = prev
        perm_head = cur
        prev = None  
        for i in range(left, right + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        perm_prev.next = prev
        perm_head.next = cur
            
        return dummy.next
            
            
            
            
        