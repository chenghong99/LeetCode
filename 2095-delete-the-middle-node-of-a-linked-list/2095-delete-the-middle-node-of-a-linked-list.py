# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        fast = head
        num = 0
        prev = dummy
        
        while fast != None:
            num += 1
            fast = fast.next
            
        num = num // 2
        
        for i in range(num):
            prev = prev.next
            head = head.next 
            
        prev.next = head.next
        
        return dummy.next
        
        
            
            
        