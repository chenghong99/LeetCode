# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(100000)
        perm_dummy = dummy
        dummy.next = head
        prev = dummy
        
        while head != None:
            if prev.val == head.val:
                while dummy.next.val != prev.val:
                    dummy = dummy.next
                    
                while head != None and prev.val == head.val:
                    prev = prev.next
                    head = head.next
                    
                dummy.next = head
                dummy = perm_dummy
            else:
                prev = prev.next
                head = head.next
        return perm_dummy.next
            
        