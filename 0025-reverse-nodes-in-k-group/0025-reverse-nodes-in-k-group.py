# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        len_of_LL = 0
        spare = head
        
        while spare != None:
            spare = spare.next
            len_of_LL += 1
            
        traversal = len_of_LL // k
        dummy = ListNode(0)
        dummy.next = head
        
        cur = head
        prev = dummy
        
        for i in range(traversal):
            perm_prev = prev
            perm_head = cur
            prev = None
            for j in range(i * k, i * k + k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            perm_prev.next = prev
            perm_head.next = cur
            prev = perm_head
            
        return dummy.next
                
                
                
            
        